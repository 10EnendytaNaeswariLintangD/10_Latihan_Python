import math

def status_bilangan_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cek_ganjil_atau_genap(n):
    if n % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
