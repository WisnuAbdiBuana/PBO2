#Suhu Celcius ke Kelvin

class Suhu:
    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273
        return k

# Contoh penggunaan
C = 8
K = Suhu.celcius_to_kelvin(C)

print("Konversi", C, "derajat Celcius adalah:", K, "derajat Kelvin")

#Latihan 2 PBO Celcius ke Reamur

class Suhu:
    @staticmethod
    def celcius_to_reamur(c):
        r = (4/5) * c
        return r

# Contoh penggunaan
C = 18
R = Suhu.celcius_to_reamur(C)

print("Konversi", C, "derajat Celcius adalah:", R, "derajat Reamur")

#Latihan 3 PBO Celcius ke Fahrenhet

class Suhu:
    @staticmethod
    def celcius_to_fahrenheit(c):
        r = (9/5) * c + 32
        return r
    
C = 10
F = (9/5) * C + 32
print("konversi ",C, "derajat Celcius adalah ",F, "derajat Fahrenheit")
