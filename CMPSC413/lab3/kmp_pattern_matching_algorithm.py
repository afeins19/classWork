"""KMP Pattern Matching Algorithm

lps_generator:
    makes the lps table for the pattern. This is then passed
    to the kmp_string_search() function to be used to make the
    search more efficient.

kmp_string_search:
    uses the lps table to traverse the text
    and avoid making unecessary comparisons.
"""

def lps_generator(pattern: str) -> []:
    pattern = list(pattern) # converts the string into a list for traversal

    lps = [0] # create a list to hold our lps table
    pattern_length = 0 # length of the current pattern
    idx = 1 # initial search position

    # search through the entire pattern
    while idx < len(pattern):

        # match
        if pattern[idx] == pattern[pattern_length]:
            lps.append(pattern_length+1) # add length+1 to position lps[idx]
            idx+=1 # increment index
            pattern_length+=1 # increment length

        # charecters don't match
        else:
            if pattern_length!=0:
                pattern_length=lps[pattern_length-1] # return len back to the last matching char
            lps.append(0) # start over again with pattern search
            idx+=1

    return lps

def kmp_string_search(text, pattern, lps=None):
    if not lps:
        lps = lps_generator(pattern)  # generate lps

    # printing data
    print("\n---- KMP Search -----")
    print(f"Text=[{text}]")
    print(f"Patt=[{pattern}]")
    print(f"\nLPS={list(pattern)}\n\t{[str(i) for i in lps]}\n")

    # declare tracking variables
    text_index, pattern_index = 0, 0
    match_idx = []  # list to store the start indices of matches

    while text_index < len(text):
        # chars match -> advance
        if text[text_index] == pattern[pattern_index]:
            pattern_index += 1
            text_index += 1

            # check for a full match of the pattern
            if pattern_index == len(pattern):
                match_idx.append(text_index - pattern_index)  # append the start index of the match
                pattern_index = lps[pattern_index - 1]  # reset pattern_index using the LPS

        # mismatch
        else:
            # if pattern_index is not 0 -> reset it using LPS to skip comparisons
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            # advance if pattern index is 0
            else:
                text_index += 1

    print(f"Match Indicies: {match_idx}")
    return match_idx

test_pattern = 'ababa'
kmp_string_search('abababbababa', test_pattern)
