def kmp_match(text, pat):
    # convert text to list
    text = list(text)

    # define an lps table
    lps = [0 for i in len(text)]

    cur_pat = 0 # iterator to hold the start of the next match search

    for i in range(len(text)):
        cur = text[i]

        while pat[cur_pat] == text[i] and i < len(text):
            lps[i] = cur_pat + 1
            cur_pat+=1
            i+=1

def make_lps(lps, pat, pat_len):
    lps_len = 0 # length of the (lps) longest prefix suffix

    lps[0] = 0
    i = 1

    while i < pat_len:
        if pat[i] == pat[pat_len]:
            pat_len+=1
            lps[i] = pat_len
            i+=1

        else:
            if pat_len != 0:
                pat_len = lps[pat_len-1]
            else:
                lps[i] = 0
                i += 1
