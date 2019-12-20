import random
import string
import os

ruta = os.path.dirname(os.path.abspath(__file__))

caracteres = string.punctuation + string.ascii_letters + string.digits
# print(f"{caracteres=}")

while True:
    while True:
        try:
            longitud = int(input('Password length?: '))
        except ValueError:
            print('Please, put a number')
        else:
            break

    password = [random.choice(caracteres) for i in range(longitud)]
    # print(password)
    password = ''.join(password)

    print(f"The password is: {password}")

    answer = input('Do you want to keep it (y/n): ').lower()

    if answer == 'y':
        break

with open(f'{ruta}\\passwords.txt','a') as fl:
    fl.write(f'{password}\n')

with open(f'{ruta}\\passwords.txt','r') as fl:
    data = fl.readlines()

for password in data:
    print(password.strip())