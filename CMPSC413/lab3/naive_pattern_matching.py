"""Simple method to compare the pattern against the text"""
def naive_pattern_match(text, pattern):
    match_idx = []

    # iterate over |text-pattern| indicies and check for the pattern one indicie higher each time
    for i in range((len(text) - len(pattern) + 1)):
        # compare the substring starting at the ith position with length pattern to pattern
        if str(text[i:len(pattern)+i]) == pattern:
            match_idx.append(i) # add to matches

    if not match_idx:
        return -1
    else:
        return match_idx

print(naive_pattern_match('ccccabcdefabc','abc'))

