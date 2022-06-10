from collections import defaultdict

# 1.1 is unique - determine if a string has all unique chars both with and without additional characters
def isUnique1(s):
    s = set()
    for c in s:
        if c in s:
            return False
        s.add(c)
    return True

def isUnique2(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                return False
    return True

# 1.2 check permutation - check if one string is a permutation of another
def checkPermutation(s, t):
    m = defaultdict(int)
    for c in s:
        m[c] += 1
    for c in t:
        if not len(m):
            return False
        if c not in m:
            return False
        m[c] -= 1
        if not m[c]:
            del m[c]
    return len(m) == 0

'''
print(checkPermutation("ilove", "olive"))
print(checkPermutation("aa", "aaa"))
print(checkPermutation("aaa", "aa"))
print(checkPermutation("robot", "roobt"))
'''

# 1.3 urlify - replace all spaces in a string with %20
def urlify(s, l):
    arr = list(s)
    j = len(arr) - 1
    for i in range(l-1, -1, -1):
        if arr[i] != " ":
            arr[j] = arr[i]
            j -= 1
        else:
            arr[j] = "0"
            arr[j-1] = "2"
            arr[j-2] = "%"
            j -= 3
    return ''.join(arr)

'''
print(urlify("Mr John Smith    ", 13))
print(urlify("ohblackbetty", 12))
print(urlify("     hello          ", 10))
'''

# 1.4 palindrome permutation - given a string, determine if it is a permutation of a palindrome
def palindromePermutation(s):
    m = defaultdict(int)
    for c in s:
        if c != " ":
            m[c] += 1
    middleCharCount = 0
    for key in m:
        if m[key] % 2 == 1:
            middleCharCount += 1
    return middleCharCount <= 1
'''
print(palindromePermutation("taco cat"))
print(palindromePermutation("tact coa"))
print(palindromePermutation("abf"))
print(palindromePermutation("aabbaa"))
print(palindromePermutation("aabaa"))
print(palindromePermutation("aaaab"))
print(palindromePermutation("aaaabb"))
print(palindromePermutation("caabb"))
print(palindromePermutation("cdaabb"))
'''

# 1.5 One Away - You are given 2 strings. An edit to a string is either
# removing a character, adding a character, or replacing a character. Determine
# if the 2 strings are at most 1 edit away. (same string is 0 edits)
def oneAway(s, t):
    if abs(len(s) - len(t)) > 1:
        return False
    mismatch = 0
    sp, tp = 0, 0
    while sp < len(s) or tp < len(t):
        if sp < len(s) and tp < len(t) and s[sp] == t[tp]:
            sp, tp = sp + 1, tp + 1
        elif mismatch == 0:
            mismatch += 1
            if len(s) == len(t):
                sp, tp = sp + 1, tp + 1
            elif len(s) > len(t):
                sp += 1
            else:
                tp += 1
        else:
            return False
    return True
'''
print("1.5 test cases")
print(oneAway("pale", "pale"))
print(oneAway("pale", "ple"))
print(oneAway("pale", "pales"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("aaaa", "aabaa"))
print(oneAway("hello", "heller"))
print(oneAway("aaa", "abaa"))
print(oneAway("abaa", "aaa"))
print(oneAway("abc", "def"))
print(oneAway("pale", "bake"))
print(oneAway("abba", "aba"))
print(oneAway("aaa", "aabc"))
'''

# 1.6 string compression - given a string with only lowercase letters a-z, write an algorithm
# that outputs the compressed string as counts of characters (i.e "aabcccdd" would be "a2b1c3d2").
# If the compressed string is not shorter than the original string, return the original string

def stringCompression(s):
    if len(s) == 0:
        return s
    temp = []
    currLetter = s[0]
    currLen = 1
    for i in range(1, len(s)):
        if s[i] != currLetter:
            temp.append(currLetter + str(currLen))
            currLetter = s[i]
            currLen = 1
        else:
            currLen += 1
    temp.append(currLetter + str(currLen))
    compressedString = ''.join(temp)
    if len(compressedString) < len(s):
        return compressedString
    return s

print("1.6 test cases")
print(stringCompression("aaaaabbccd"))
print(stringCompression("abcde"))
print(stringCompression("aabcccccaaa"))
print(stringCompression("aaaaa"))




