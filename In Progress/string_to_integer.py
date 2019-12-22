class Solution:
    def myAtoi(self, str: str) -> int:
        str.replace(" ","")
        return int(str)

if (__name__ == "__main__"):
    string = " 1"
    a = "-91283472332"

    obj = Solution()
    print("Integer : {}".format(obj.myAtoi(string)))
