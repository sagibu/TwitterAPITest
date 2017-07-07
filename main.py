from twython import Twython
import json

def main():
    with open('settings.json') as settings_json:
        settings = json.load(settings_json)
    twitter = Twython(settings['APP_KEY'], settings['APP_SECRET'], oauth_version=2, access_token=settings['ACCESS_TOKEN'])

    result = twitter.search(q='NBA', result_type='recent', count=100)
    x = 0
    for t in result['statuses']:
        x += 1
        print(t['text'])
        print("===================================END==============================")

    print(x)
if __name__ == "__main__":
    main()