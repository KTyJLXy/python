def check_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if ''.join(sorted(word1)) == ''.join(sorted(word2)):
        return True
    else:
        return False

def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if len(word) == len(candidate) and word.lower() != candidate.lower():
            if check_anagram(word, candidate) == True:
                anagrams.append(candidate)
    return anagrams