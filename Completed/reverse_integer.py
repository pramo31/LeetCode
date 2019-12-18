class Solution:
    def reverse(self, x: int) -> int:
        max = 2 ** 31 - 1
        min = -1 * 2 ** 31
        if (not min < x < max):
            return 0
        isNegative = False
        if (x < 0):
            isNegative = True
            x = x * -1
        str_x = str(x)[::-1]
        num = int(str_x)
        num = num * -1 if isNegative else num
        return 0 if not min < num < max else num


if (__name__ == "__main__"):
    num = 1534236469

    obj = Solution()
    print(obj.reverse(num))
