import random

guesses_made = 0

print ' \n'
print ' \n'
print ' \n'
print 'Hello, world!\n'

name = raw_input('Hi there. What is your name?\n')

number = random.randint(1, 20)

print 'Okay, {0}, I chose a number between 1 and 20.'.format(name)

while guesses_made < 6:

    guess = int(raw_input('Try and guess it: '))

    guesses_made += 1

    if guess < number:
        print 'Too low.'

    if guess > number:
        print 'Too high.'

    if guess == number:
        break

if guess == number:
    print 'Well done, {0}! You guessed the number in {1} tries!'.format(name, guesses_made)
else:
    print 'Nope. Sorry, the number I chose was {0}'.format(number)