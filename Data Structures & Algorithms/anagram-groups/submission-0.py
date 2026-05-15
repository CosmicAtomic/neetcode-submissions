class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}
        for word in strs:
            sorted_word = "".join(sorted(word)) 
            if sorted_word not in anagram_hash:
                anagram_hash[sorted_word] = [word]
            else:
                anagram_hash[sorted_word].append(word)
        output = [value for value in anagram_hash.values()]
        return output


        