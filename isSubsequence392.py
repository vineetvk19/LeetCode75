class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        sp = 0
        i = 0
        while i<len(t) and sp<len(s):
            if t[i] == s[sp]:
                sp+=1
            if sp == len(s):
                return True
            i+=1
        return False
