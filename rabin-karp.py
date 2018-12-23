d = 256


def rabin_karp(text, pattern, q):
    m = len(pattern)
    n = len(text)
    i, j, p, t, h = 0, 0, 0, 0, 1

    for i in xrange(m - 1):
        h = (h * d) % q

    for i in xrange(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in xrange(n - m + 1):
        if p == t:
            for j in xrange(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print "pattern found at index " + str(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t += q


rabin_karp("geeks for geek", "eek", 101)
