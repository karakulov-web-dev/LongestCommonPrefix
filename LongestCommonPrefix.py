class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.longestCommonPrefixUseZip(strs)

    def longestCommonPrefixUseZip(self, strs):
        result = ''
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                result += chars[0]
            else:
                break
        return result

    def longestCommonPrefixUseFor(self, strs):
        minLength = min(len(s) for s in strs)
        result = ''
        for i in range(minLength):
            isEqual = self.check(strs, i)
            if isEqual:
                result += self.getChar(strs[0], i)
            else:
                return result
        return result

    def check(self, strs, index):
        result = True
        char = self.getChar(strs[0], index)
        if char is None:
            return False
        for currentString in strs:
            currentChar = self.getChar(currentString, index)
            if char != currentChar:
                result = False
                break
        return result

    def getChar(self, string, index):
        if len(string) - 1 < index:
            return None
        else:
            return string[index]