import random

secret_number =random.randint(1, 10)

guess = int(input("Masukkan tebakanmu: "))

if guess > secret_number:
    print("Too high.")
elif guess < secret_number:
    print("Too low.")
else:
    print("Gokil ! kamu hebat ! mamah bangga sama kamu !")

print("jawaban benar adalah", secret_number)