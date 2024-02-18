class FastPrime:
    def __init__(self, N):
        self.n = N
        self.prime = [1] * (self.n + 1)
        self.spf = [-1] * (self.n + 1)

    def populate_spf(self):
        self.prime[1] = 0
        i = 2
        while i * i <= self.n:
            if self.prime[i] == 1:
                j = i
                while i * j <= self.n:
                    if self.spf[i * j] == -1:
                        self.spf[i * j] = i
                        self.prime[i * j] = 0
                    j += 1

            i += 1

    def print_prime_factorization(self, num):
        while self.spf[num] != -1:
            print(f"{self.spf[num]}*", end="")
            num = num // self.spf[num]
        if num != 1:
            print(f"{num}")


if __name__ == "__main__":
    fp = FastPrime(10000)
    fp.populate_spf()
    fp.print_prime_factorization(6060)
