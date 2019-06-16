def check_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    for char in word1:
        if char not in word2:
            return False
    for char in word1
    return True

def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if len(word) == len(candidate) and word.lower() != candidate.lower():
            if check_anagram(word, candidate) == True:
                anagrams.append(candidate)
    return anagrams