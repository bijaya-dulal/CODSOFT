import random
import string

length = int(input('enter the length of the password'))
complex

#function to generate the password of given length
def gen_pas(len):
    length= len
    #define the characters  to include in password
    characters = string.ascii_letters + string.digits + string.punctuation

    random_pwd = ''.join(random.choice(characters) for _ in range(length))

    return random_pwd
print(gen_pas(length))    
  