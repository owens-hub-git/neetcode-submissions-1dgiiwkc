class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if len(word) == 1:
            return 0

        table = {}

        for i in range(len(keyboard)):
            table[keyboard[i]] = i

        res = 0
        prev = 0

        for letter in word:
            add = table[letter]
            res += abs(add - prev)
            prev = table[letter]

        return res