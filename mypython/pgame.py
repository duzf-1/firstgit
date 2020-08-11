import random
secret = random.randint(1,10)
print('---this is a game----')
temp = input('please enter a luck number:')
guess = int(temp)
while guess != secret:
    temp = input('no no no ,guess again:')
    guess = int(temp)
    if guess == secret:
        print('yes, you get it. /n enn, that is still no gift')
    else:
        if guess < secret:
            print('too small, please biger')
        else:
            print('oh, please smaller')
print('I am tired, game over')
