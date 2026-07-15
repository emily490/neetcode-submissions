class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = []
        sArr = []
        tArr = []
        for i in range(len(s)):
            temp.append(ord(s[i]))
        temp.sort()
        sArr = temp
        temp = []
        for i in range(len(t)):
            temp.append(ord(t[i]))
        temp.sort()
        tArr = temp
        for i in range(len(sArr)):
            if sArr[i] != tArr[i]:
                return False
        return True
