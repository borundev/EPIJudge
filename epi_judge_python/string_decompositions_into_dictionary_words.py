from typing import List
from collections import Counter
from test_framework import generic_test

def find_all_substrings(s: str, words: List[str]) -> List[int]:

    """
    The solution is a bit different from the one in the book in that we maintain a sliding window counter.
    We only check match_all_words if the counter matches the counter for the characters in the words
    :param s:
    :param words:
    :return:
    """

    def match_all_words(start):
        cur_word_counter=Counter()
        for i in range(start,start+n*m,m):
            cur_word=s[i:i+m]
            it=word_to_freq[cur_word]

            if it==0:
                # word doesn't exist in words
                return False

            cur_word_counter[cur_word]+=1

            if cur_word_counter[cur_word]>it:
                # word exists in current substring more often than in words
                return False

        return True

    # counter for all characters in words
    c_words=Counter(''.join(words))
    # counter for all words in the list words
    word_to_freq = Counter(words)

    n=len(words)
    m=len(words[0])
    result = []

    tl=n*m
    c_substring=Counter(s[:tl])
    if c_words==c_substring and match_all_words(0):
        result.append(0)

    for i in range(tl,len(s)):
        c_substring[s[i]]+=1
        if c_substring[s[i-tl]]>1:
            c_substring[s[i - tl]] -= 1
        else:
            del c_substring[s[i-tl]]

        if c_words==c_substring and match_all_words(i-tl+1):
            result.append(i-tl+1)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))


