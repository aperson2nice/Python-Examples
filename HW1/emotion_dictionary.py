#Sheila Robles
#Assignment 1 Problem 4
#Python Version 3.0.1

'''
*<|:-) santa clause
<3 heart
>:( angry
>:) evil
@}-;-'-- rose
O:-) angel
'''

emotions = {"santa clause":"*<|:-)","heart":"<3", "angry":">:(",
		   "evil":">:)","angel":"O:-)","rose":"@}-;-'--"}

emote = input("Enter and emote name: ")
print(emotions.get(emote))
