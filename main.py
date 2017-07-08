from FrequentWordCalculator import FrequentWordCalculator
import time


def main():
    frequent_words = FrequentWordCalculator('settings.json')
    # frequent_words.monitor_topic("dota", 1800.0)
    # frequent_words.monitor_topic("NBA", 1800.0)
    # frequent_words.monitor_topic("hearthstone", 1800.0)
    print(frequent_words.most_frequent_words("dota"))

    while True:
        time.sleep(100)

if __name__ == "__main__":
    main()