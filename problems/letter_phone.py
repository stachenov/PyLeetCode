class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits:
            return res
        mapping = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': 'tuv', '9': "wxyz"}
        def combinations(prefix, digits):
            if not digits:
                res.append(prefix)
                return
            for c in mapping[digits[0]]:
                combinations(prefix + c, digits[1:])
        combinations("", digits)
        return res
