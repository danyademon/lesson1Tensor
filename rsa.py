import random
from math import gcd as bltin_gcd

def Ferma(n, t):
    for i in range(t):
        a = random.randint(2, n - 2)
        if pow(a, (n - 1), n) != 1:
            return -1
    return n


def generate_prime_number():
    while (True):
        prime_num = "1"
        while (len(prime_num) < 512):
            prime_num += str(random.randint(0, 1))
        prime_num += "1"
        prime_num = int(prime_num, 2)
        if (Ferma(prime_num, 50) != -1):
            return prime_num

def functionEiler(p,q):
    return (p-1)*(q-1)

def generateE(eiler,n):
    while True:
        r = random.randint(3, n-2)
        if (bltin_gcd(eiler, r) == 1):
            return r

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generateKeys():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p*q
    eiler=functionEiler(p,q)
    e=generateE(eiler,n)
    gcd, x, y = gcdExtended(e, eiler)
    d = (x % eiler + eiler) % eiler
    openKey=[e,n]
    privateKey=[d,n]
    return openKey,privateKey

def encrypt(message,openkey):
    return pow(message,openkey[0],openkey[1])

def decrypt(message, privateKey):
    return pow(message,privateKey[0],privateKey[1])


print('Введите число')
message=int(input())
openKey,privateKey=generateKeys()
# openKey=[13718477,21633727]
# privateKey=[93,21633727]
print("Результат шифрования")
shifrtext=encrypt(message,openKey)
print(shifrtext)
print("Результат дешифрования")
text=decrypt(shifrtext,privateKey)
print(text)
