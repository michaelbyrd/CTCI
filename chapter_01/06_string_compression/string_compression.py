# Chapter 1 | Arrays and Strings
# Problem 1.6 — String Compression
#
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string "aabcccccaaa" would become
# "a2b1c5a3". If the compressed string would not be smaller than the original
# string, return the original string.
#
# Example:
#   Input:  "aabcccccaaa"
#   Output: "a2b1c5a3"


# v1 — Time: O(n²), Space: O(n)
#   str += creates a new string each iteration, making it O(n) per append → O(n²) overall
def string_compression(s):
    out, i, c = "", 0, 0
    current = s[i]
    out += current


    while i < len(s):
        if current == s[i]:
            c += 1
        else: 
            out += str(c)
            current = s[i]
            out += current
            c = 1
        i += 1

    out += str(c)
    if len(out) >= len(s):
        return s

    return out


# v2 — Time: O(n), Space: O(n)
#   list append is O(1), join is O(n) once at the end — true linear time
def string_compression_v2(s):
    out, i, c = [], 0, 0
    current = s[i]
    out.append(current)


    while i < len(s):
        if current == s[i]:
            c += 1
        else:
            current = s[i]
            out += [str(c), current]
            c = 1
        i += 1

    out.append(str(c))
    if len(out) >= len(s):
        return s

    return "".join(out)


# v3 — Time: O(n) best case, O(2n) worst case. Space: O(1) for incompressible, O(n) for compressible
#   incompressible: one pass only, no output allocated → best real-world performance when inputs rarely compress
#   compressible: two full passes → same O(n) but higher constant than v2
def string_compression_v3(s):
    # first pass: calculate compressed length without building output
    compressed_len, i, c = 0, 0, 0
    current = s[0]
    while i < len(s):
        if s[i] == current:
            c += 1
        else:
            compressed_len += 1 + len(str(c))
            current = s[i]
            c = 1
        i += 1
    compressed_len += 1 + len(str(c))

    if compressed_len >= len(s):
        return s

    # second pass: build output only if compression is worthwhile
    out, i, c = [], 0, 0
    current = s[0]
    while i < len(s):
        if s[i] == current:
            c += 1
        else:
            out += [current, str(c)]
            current = s[i]
            c = 1
        i += 1
    out += [current, str(c)]

    return "".join(out)