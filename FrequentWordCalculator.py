from TwitterAPIHandler import TwitterAPIHandler
from TwitterDBHandler import TwitterDBHandler
import threading


class FrequentWordCalculator:
    def __init__(self, settings_file):
        self.db_handler = TwitterDBHandler(settings_file)
        self.twitter_handler = TwitterAPIHandler(settings_file)

    def query_topic(self, topic, query_type):
        tweets = self.twitter_handler.query_new_tweets(topic, query_type)
        if not self.db_handler.table_exists(topic):
            self.db_handler.create_tweets_table(topic)
        self.db_handler.add_list_to_table(tweets, topic)

    def monitor_topic(self, topic, delay):
        self.query_topic(topic, 'recent')
        threading.Timer(delay, self.monitor_topic, [topic]).start()
