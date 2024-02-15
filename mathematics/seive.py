class Sieve:
    def __init__(self, N) -> None:
        self.n = N
        self.isPrime = [0] * (self.n + 1)

    def sieve_process(self):
        self.isPrime[1] = 1
        i = 2
        while i * i <= self.n:
            if not self.isPrime[i]:
                j = i
                while i * j <= self.n:
                    self.isPrime[i * j] = 1
                    j += 1
            i += 1
        for k in range(1, self.n + 1):
            if not self.isPrime[k]:
                print(k, end=" ")


if __name__ == "__main__":
    N = int(input())
    s = Sieve(N)
    s.sieve_process()
