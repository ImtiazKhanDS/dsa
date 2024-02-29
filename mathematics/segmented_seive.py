import math


class SegmentedSieve:
    def __init__(self, N):
        self.n = N
        self.is_prime = [1] * (self.n + 1)
        self.primes = []

    def populate_primes(self):
        self.is_prime[1] = 0
        i = 2
        while i * i <= self.n:
            if self.is_prime[i]:
                j = i
                while i * j <= self.n:
                    self.is_prime[i * j] = 0
                    j += 1
            i += 1
        for k in range(1, self.n + 1):
            if self.is_prime[k]:
                self.primes.append(k)

    def get_prime_in_range(self, L, R):
        primes_range = [1] * (R - L + 1)
        for x in self.primes:
            k = math.ceil(L / x)

            j = max(k, 2)
            while j * x <= R:
                primes_range[j * x - L] = 0
                j += 1

        ans = []
        for i, x in enumerate(primes_range):
            if x:
                ans.append(i + L)
        return ans


if __name__ == "__main__":
    ss = SegmentedSieve(1000000)
    ss.populate_primes()
    R = 99
    L = 90
    out = ss.get_prime_in_range(L, R)
    print(out)
