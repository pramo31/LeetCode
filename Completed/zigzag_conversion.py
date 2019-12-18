from builtins import str


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        length = len(s)
        magicNumber = numRows * 2 - 2
        if (numRows == 1):
            return s
        if (length == 0):
            return result
        else:
            divNum = 0
            for i in range(1, numRows + 1):
                index = i
                binary = 0
                while (index <= length):
                    result += s[index - 1]
                    if (divNum == 0 or divNum == magicNumber):
                        index += (magicNumber)
                    else:
                        if (binary == 0):
                            index += (magicNumber - divNum)
                        else:
                            index += divNum
                    binary = 0 if binary == 1 else 1
                divNum += 2
        return result


if (__name__ == "__main__"):
    s = "PAYPALISHIRING"

    obj = Solution()
    print(obj.convert(s, 4))
