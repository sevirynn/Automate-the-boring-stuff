#This is the lesson from Chatper 1 of Al Sweigart's "Automate the Boring Stuff with Python"
# This program says hello, asks for my name, tells me the length of my name, asks how old I am then adds 1 to figure out my age next year.
print ('Hello, world!')
print ('What is your name?')
myName = input()
print ('It is good to meet you, ' + myName)
print ('The length of your name is:')
print (len(myName))
print ('What is your age?')
myAge = input()
print ('You will be ' +str(int(myAge) + 1) + ' in a year.')