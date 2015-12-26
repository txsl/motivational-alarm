import datetime
import subprocess

from gtts import gTTS

deadline = datetime.datetime(year=2015, month=06, day=17, minute=00, hour=16)

time_remaining = deadline - datetime.datetime.now()



time_remaining_str = "It's time for you to go home. Good news: only %i days of your degree left. The Triple E Department thank you for working hard on your projects." % (time_remaining.days,)
ts = gTTS(text=time_remaining_str, lang='en')
ts.save('time_remaining.mp3')

try:
    subprocess.call(['cvlc', '--play-and-exit', '--volume', '500', 'time_remaining.mp3'])
except OSError:
    subprocess.call(['mpg123', 'time_remaining.mp3'])