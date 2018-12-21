def compute_lps_array(pat, m, lps):
    lps[0] = 0

    j = 0
    for i in range(1, m):
        if pat[j] == pat[i]:
            lps[i] = j + 1
            j += 1
            i += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            lps[i] = j + 1
            i += 1


def kmp_search(pat, txt):
    m = len(pat)
    n = len(txt)

    # Create lps array that will hold the longest prefix suffix
    lps = [0] * m

    # Preprocess the pattern (calculate the lps)
    compute_lps_array(pat, m, lps)

    i = 0
    j = 0
    while i < n:
        if pat[j] == txt[i]:
            j += 1
            i += 1

        if j == m:
            print "Pattern found at index " + str(i - j)
            j = lps[j - 1]
        # mismatch after j matches
        elif i < n and pat[j] != txt[i]:
            # Do not match lps[0..lps[j - 1]] characters, they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


kmp_search("ABBA", "ASDABBASABABABBAdfdABBA")
