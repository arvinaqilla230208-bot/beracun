import random

choose = input("Pilih level (1-3): ")

if choose == "1":
    secret_number = random.randint(1, 10)
elif choose == "2":
    secret_number = random.randint(1, 50)
else:
    secret_number = random.randint(1, 100)


guess = 0

while guess != secret_number:
    guess = int(input("Masukkan tebakanmu: "))
    
    if guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Correct!")