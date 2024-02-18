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
        print(f"prime numbers : {self.prime}")
        print(f"smallest prime factor : {self.spf}")


if __name__ == "__main__":
    fp = FastPrime(10)
    fp.populate_spf()
