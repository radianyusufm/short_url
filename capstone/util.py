import random

def generate_slug():
    character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    temp = ''
    for i in range(1,8) :
        temp = temp + ''.join(random.choice(character))

    return temp

print(generate_slug())