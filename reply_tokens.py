from datetime import datetime
import random

greeting_spellings = ['good', 'gd', 'gud', 'goood']

wish_spellings = ['morning', 'mrng', 'mng', 'mngg', 'evening', 'eve', 'evng', 'evez', 'eveng', 'noon', 'afternoon', 'after noon', 'aftrnoon', 'aftr noon']

morning_wishes = [
					'Good morning! Have a great day. :sunrise:',
					'Good morning. :sunny:',
					'Good morning. Hope you are doing great. :slightly_smiling_face:',
					'Already morning? I am still at my bed. :zzz:'
				 ]

noon_wishes = [
				'Good noon! Had your lunch? :curry:',
				'Good afternoon. Am feeling sleepy. What are you upto?',
				'Good noon. Feeling sleepy? :sleeping:',
				'Good noon. Already it\'s noon, I haven\'t even ate my breakfast!'
			 ]

def greet_user(command):
	"""
		Used for replying 'Good Morning' kind of greetings from users.
	"""
	if any(elt in command for elt in greeting_spellings):
		if any(elt in command for elt in wish_spellings):
			hour = datetime.now().time().hour
			if 0 <=  hour <= 11:
				return random.choice(morning_wishes)
			elif 11 < hour <= 15:
				return random.choice(noon_wishes)
			elif 15 < hour <= 19:
				return 'Good evening! Hope you are enjoying the day.'
			elif 19 < hour <= 23:
				return 'Good night! Sleep tight. Sweet dreams.'
			else:
				return False