class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(21, 4)) 
print(Kalkulator.subtract(21, 4)) 
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(3, 10)) 
print(Kalkulator.divide(100, 15)) 
