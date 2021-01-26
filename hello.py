# hello.py
import random

print("Hello World!")
abcd = "qwertyuiopasdfghjklzxcvbnm1234567890-=+_)(*&^%$#@!QWERTYUIOPASDFGHJKLZXCVBNM"

def gen_pas(n=12):
    r = ""
    for i in range(n):
        r += random.choice(abcd)
    print(r)

gen_pas()
