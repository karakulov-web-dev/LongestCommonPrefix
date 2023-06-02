class Solution:
    def longestCommonPrefix(self, strs) -> str:
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
            isEqual = check(strs, i)
            if isEqual:
                result += getChar(strs[0], i)
            else:
                return result
        return result

solution = Solution()