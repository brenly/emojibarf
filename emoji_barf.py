##this code simply outputs a random string of 20 emojis that carry angry/ violent connotation. for humorous purposes.
##this was an exercise in printing out emojis in python/ terminal for other unicode projects i am working on.
##brenly

##import pyperclip
##oops! pypercip does not suport unicode!

import random
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)


emojilist = [u'\U0001F52B', u'\U0001F3F4', u'\U0001F48A', u'\U0001F52A', u'\U00002694', u'\U0001F6E2', u'\U0001F489', u'\U0001F620', u'\U0001F4A3', u'\U0001F3F9', u'\U0001F5E1', u'\U000026B0']
## black flag, gun, pill, knife, crossed swords, oil barrel, needle emoji, angry emoji, bomb emoji, bow arrow, dagger, casket
## this is not an EXACT key, just to keep track so i didn't double up on emojis

##sys.stdout for no \newline whitespaces.

for i in range(20):
	sys.stdout.write(emojilist[random.randint(0, 11)])

print "\n"
