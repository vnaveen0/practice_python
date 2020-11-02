class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sentence = s.split()
        new_sentence = ''
        L = len(sentence)
        for idx, word in enumerate(sentence):
            def reverse(w):
                Len = len(w)
                new_w = ''
                for i in reversed(range(Len)):
                    new_w = new_w + w[i]
                return new_w
            
            new_word = reverse(word)
            new_sentence = new_sentence + new_word
            if idx != L -1:
                new_sentence = new_sentence + ' '
        return new_sentence
        
