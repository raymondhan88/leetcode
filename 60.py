class Solution:
    @classmethod
    def getPermutation(self, n: int, k: int) -> str:
        t = n
        for i in range(1, n):
            t *= i
        valid = [1] * n
        res = ""
        k -= 1
        for i in range(n, 0, -1):
            t //= i
            seq = k // t
            for j in range(n):
                seq -= valid[j]
                if seq < 0:
                    res += str(j + 1)
                    valid[j] = 0
                    break
            k %= t

        return str(res)


if __name__ == "__main__":
    print(Solution.getPermutation(3,3))