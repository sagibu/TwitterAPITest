#!flask/bin/python
from FrequentWordCalculator import FrequentWordCalculator
import time
from app import app


def main():
    # frequent_words = FrequentWordCalculator('settings/settings.json')
    # frequent_words.monitor_topic("dota", 1800.0)
    # frequent_words.monitor_topic("NBA", 1800.0)
    # frequent_words.monitor_topic("hearthstone", 1800.0)
    #
    # while True:
    #     print(frequent_words.most_frequent_words("dota"))
    #     print(frequent_words.most_frequent_words("NBA"))
    #     print(frequent_words.most_frequent_words("hearthstone"))
    #     time.sleep(100)

    app.run(debug=True)

if __name__ == "__main__":
    main()