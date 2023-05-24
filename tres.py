import sys, random, requests, time, argparse

# Initialize the parser
parser = argparse.ArgumentParser(
    prog='tres',
    description='Just a simple Polaris XP farmer',
    epilog='https://github.com/ShadowFire5650/Tres/'
)
parser.add_argument('token', type=str)
parser.add_argument('channel', type=int)
parser.add_argument('-m', '--msgs', default=64, type=int)
parser.add_argument('-w', '--words', default=5, type=int)
parser.add_argument('-d', '--delay', default=0.5, type=float)
args = parser.parse_args()

# Get the list of words.
link = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
f = requests.get(link)
words = f.text.split('\n')

# Load Config
msgs = args.msgs
words_per_msg = args.words
delay = args.delay
channel = args.channel
token = args.token

# Initialize Variables
total_words, completed_words, completed_msgs = msgs * words_per_msg, 0, 0
post_url = "https://discord.com/api/v9/channels/%d/messages" % channel
headers = {
    'authorization': token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

# Begin!
try:
    for i in range(msgs):
        sys.stdout.flush()
        payload = {
            'content': ' '.join(random.sample(words, words_per_msg))
        }
        r = requests.post(post_url, data=payload, headers=headers)
        if r.status_code != 200:
            print("\x1b[38;2;194;29;17mTask failed with status code %d\x1b[0m" % r.status_code)
            exit(0)
        time.sleep(delay)
        completed_words += words_per_msg
        completed_msgs += 1
        sys.stdout.write(
            f"\r\x1b[38;2;252;186;3m{completed_words}/{total_words} Words | {completed_msgs}/{msgs} Messages\x1b[0m",
        )
except KeyboardInterrupt:
    quit(0)
