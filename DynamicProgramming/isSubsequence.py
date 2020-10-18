class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_substr = len(s)
        j = 0

        if not s:
            return True

        if not t:
            return False

        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1

            if j >= len_substr:
                return True

        # --
        return False