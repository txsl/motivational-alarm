import datetime
import random
import subprocess

from gtts import gTTS

try:
    read_quotes_f = open('already_read.txt', 'r')
    read_quotes = [line.rstrip('\n') for line in read_quotes_f]

except IOError:
    read_quotes_f = open('already_read.txt', 'w')
    read_quotes = []

read_quotes_f.close()

print read_quotes

all_quotes = [line.rstrip('\n') for line in open('quotes.txt')]

all_quotes_not_read = [q for q in all_quotes if q not in read_quotes]

if len(all_quotes_not_read) == 0:
    all_quotes_not_read = all_quotes
    open('already_read.txt', 'w').close()


deadline = datetime.datetime(year=2015, month=06, day=17, minute=00, hour=16)

time_remaining = deadline - datetime.datetime.now()

motivational_quote = random.choice(all_quotes_not_read)


time_remaining_str = "%i days and %i hours remaining. %s" % (time_remaining.days, time_remaining.seconds // 3600, motivational_quote)

ts = gTTS(text=time_remaining_str, lang='en')
ts.save('time_remaining.mp3')

try:
    subprocess.call(['cvlc', '--play-and-exit', '--volume', '500', 'time_remaining.mp3'])
except OSError:
    subprocess.call(['mpg123', 'time_remaining.mp3'])

read_quotes_f = open('already_read.txt', 'a')

read_quotes_f.write(motivational_quote + '\n')
read_quotes_f.close()

