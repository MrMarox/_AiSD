def prime(n: int) -> bool:
    if n < 2:
        return False
    if n / prime(n - 1) == 0:
           return True


print(prime(3))
