class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if len(s.strip()) == 0:
            return s.strip()
        s = s.strip()
        out = ""
        word = ""
        for ch in s:
            if not ch.isspace():
                word += ch
            else:
                if len(out) == 0:
                    out = word
                elif len(word.strip()) > 0:
                    out = word + " " + out
                word = ""
        out = word + " " + out
        out = out.strip()
        return out
