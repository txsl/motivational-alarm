import datetime
import random
import subprocess

from gtts import gTTS

quotes = [line.rstrip('\n') for line in open('quotes.txt')]

deadline = datetime.datetime(year=2015, month=06, day=17, minute=00, hour=16)

time_remaining = deadline - datetime.datetime.now()


time_remaining_str = "%i days and %i hours remaining. %s" % (time_remaining.days, time_remaining.seconds // 3600, random.choice(quotes))

ts = gTTS(text=time_remaining_str, lang='en')
ts.save('time_remaining.mp3')

subprocess.call(['cvlc', '--play-and-exit', '--volume 500', 'time_remaining.mp3'])

