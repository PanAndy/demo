
import math

class Solution:

    def solve(self, n, l, r):
        list_n = [n]
        while True:
            flag = False
            for i in range(len(list_n)):
                if list_n[i] > 1:
                    flag = True
                    t = self.convert(list_n[i])
                    list_n[i] = t[0]
                    for j in range(len(t) - 1):
                        list_n.insert(i, t[j])
            if flag is False:
                break

        ret = 0
        for i in range(l, r):
            if list_n[i-1] == 1:
                ret += 1
        return ret

    def convert(self, n):
        list_n = [None, None, None]
        list_n[0] = math.floor(n / 2)
        list_n[1] = n % 2
        list_n[2] = list_n[0]
        return list_n


if __name__ == "__main__":
    t = Solution().solve(10, 3, 10)
    print(t)
