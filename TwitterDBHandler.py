import psycopg2
import json


class TwitterDBHandler:
    def __init__(self, settings_file):
        with open(settings_file) as settings_json:
            settings = json.load(settings_json)['DB']
        try:
            self.conn = psycopg2.connect(
                "dbname={} user={} host={} port={} password={}".format(settings['DBNAME'],
                                                                       settings['USER'],
                                                                       settings['HOST'],
                                                                       settings['PORT'],
                                                                       settings['PASSWORD']))

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tweets_table(self, topic):
        try:
            cur = self.conn.cursor()
            sql = """
            CREATE TABLE {0}_tweets (
                tweet_creation_time timestamp,
                tweet_text character varying
            );
            ALTER TABLE ONLY  {0}_tweets ADD CONSTRAINT {0}_text_ctime PRIMARY KEY (tweet_creation_time,tweet_text);
            """.format(topic)
            cur.execute(sql)
            cur.close()
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(error)

    def add_tweet_to_table(self, tweet, topic):
        try:
            cur = self.conn.cursor()
            sql = """INSERT INTO public.{}_tweets(tweet_creation_time, tweet_text)
                        VALUES(%s,%s)""".format(topic)
            cur.execute(sql, (tweet['created_at'], tweet['text']))
            cur.close()
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()

    def add_list_to_table(self, tweets_list, topic):
        for tweet in tweets_list:
            self.add_tweet_to_table(tweet, topic)

    def table_exists(self, topic):
        try:
            cur = self.conn.cursor()
            cur.execute("select exists(select * from information_schema.tables where table_name=%s)",
                        ("{}_tweets".format(topic),))
            exists = cur.fetchone()[0]
            cur.close()
            return exists

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()
            return False

    def most_frequent_words(self, topic):
        try:
            cur = self.conn.cursor()
            sql = """
            SELECT word, ct FROM (
                SELECT unnest(string_to_array(tweet_text, ' ')) AS word, count(*) AS ct
                FROM   public.{}_tweets
                GROUP  BY 1
                ORDER  BY 2 DESC
                ) words
                WHERE word ~ '^[\w,@,#]+$'
                LIMIT 50
            """.format(topic)
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows

        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(error)

    def total_number_of_rows(self, topic):
        try:
            cur = self.conn.cursor()
            sql = """
            SELECT COUNT(*) FROM {}_tweets
            """.format(topic)
            cur.execute(sql)
            result = cur.fetchone()
            cur.close()
            return result[0]

        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(error)