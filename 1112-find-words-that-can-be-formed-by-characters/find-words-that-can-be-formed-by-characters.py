from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count=Counter(chars)
        total_length=0
        for i in words:
            word_count=Counter(i)
            if all(word_count[char]<=char_count[char] for char in i):
                total_length+=len(i)
        return total_length
        