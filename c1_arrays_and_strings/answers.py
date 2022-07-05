from collections import defaultdict, deque
import random

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

'''
print("1.6 test cases")
print(stringCompression("aaaaabbccd"))
print(stringCompression("abcde"))
print(stringCompression("aabcccccaaa"))
print(stringCompression("aaaaa"))
'''

# 1.7 rotate matrix - rotate a matrix by 90 degrees
'''
n=6
layer0: layer0 layer1 layer2 layer3 layer4 [0, n-1)
layer1: layer0 layer1 layer2 [0, n-3)
layer2: layer0 [0, n-5)

n=5
layer0: layer+0 layer+1 layer+2 layer+3 [0, n-1)
layer1: layer+0, layer+1 [0, n-3)
layer2: layer+0 [0, n-4)

n=4
layer0: layer0, layer1, layer2 [0, n-1)
layer1: layer0 [0, n-3]

n=3
layer0, layer1
layer0
'''
def rotateMatrix(grid, n):
    numLayers = n // 2 if n % 2 == 0 else n // 2 + 1
    for layer in range(numLayers):
        top = layer
        right = n-1-layer
        left = layer
        bottom = n-1-layer
        for i in range(right-left):
            temp = grid[bottom-i][left]
            grid[bottom-i][left] = grid[bottom][right-i]
            grid[bottom][right-i] = grid[top+i][right]
            grid[top+i][right] = grid[top][left+i]
            grid[top][left+i] = temp
    return grid

'''
print("1.7 test cases")
print(rotateMatrix([[1, 2], [3, 4]], 2))
print(rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4))
print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]], 3))
print(rotateMatrix([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], 4))
'''

# 1.8 zero matrix - given a matrix, if matrix[i][j] == 0, then set all elements in row i 
# and all elements in column j to 0. matrix may not be square. 

def zeroMatrix(matrix, m, n):
    rows = set()
    cols = set()
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)
    for row in range(m):
        for col in range(n):
            if row in rows or col in cols:
                matrix[row][col] = 0

'''
print("1.8 test cases")
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
zeroMatrix(matrix, 4, 3)
print(matrix)
matrix = [[0]]
zeroMatrix(matrix, 1, 1)
print(matrix)
matrix = [[3]]
zeroMatrix(matrix, 1, 1)
print(matrix)
'''

# 1.9 String rotation - assume you have a method isSubstring that tells if you one string is a 
# substring of another. Given 2 strings s1 and s2, write an algorithm to tell if s2 is a rotation
# of s1 using only 1 call to isSubstring. ex) waterbottle erbottlewat

# Had to look at all 3 hints.
def stringRotation(s1, s2):
    temp = s2 + s2
    return isSubstring(s1, temp)

# stub method
def isSubstring(a1, a2):
    pass

'''
16.8 english int - given any integer, print an english phrase that describes the integer

ex) 1234 = "One thousand two hundred thirty four
1024 = one thousand twenty four
Approach: chunk it into groups of 3
'''

def englishInt(n):
    if n == 0:
        return "zero"
    def getDigits(n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        return digits

    base = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen"
    }

    mid = {
        2: "twen",
        3: "thir",
        4: "four",
        5: "fif",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    if n <= 13:
        return base[n]

    def triplets(digits):
        if len(digits) == 1:
            if digits[0] == 0:
                return ""
            return base[digits[0]]
        if len(digits) == 2:
            if digits[1] == 0:
                 return triplets(digits[:1])
            if digits[1] == 1:
                if digits[0] + 10 <= 13:
                    return base[digits[0]+10]
                return mid[digits[0]] + "teen"
            else:
                initial = mid[digits[1]] + "ty"
                end = triplets(digits[:1])
                if len(end):
                    initial += " " + end
                return initial
        if len(digits) == 3:
            if digits[2] == 0:
                return triplets(digits[:2])
            initial = base[digits[2]] + " hundred"
            end = triplets(digits[:2])
            if len(end):
                initial += " " + end
            return initial

    suffixes = ["", " thousand", " million", " billion", " trillion"]
    digits = getDigits(n)
    i = 0
    pow = 0
    solution = []
    while i < len(digits):
        chunk = []
        if i + 2 < len(digits):
            chunk = digits[i:i+3]
        elif i + 1 < len(digits):
            chunk = digits[i:i+2]
        else:
            chunk = [digits[i]]
        tripletValue = triplets(chunk)
        if len(tripletValue):
            solution.append(suffixes[pow // 3])
        solution.append(tripletValue)
        solution.append(" ")
        pow += 3
        i += 3
    if solution[-1] == " ":
        solution.pop()
    return ''.join(solution[::-1])

'''
print("16.8 test cases")
print(englishInt(100))
print(englishInt(102))
print(englishInt(123))
print(englishInt(12))
print(englishInt(99))
print(englishInt(27))
print(englishInt(15))
print(englishInt(1234))
print(englishInt(1024))
print(englishInt(10000))
print(englishInt(112))
print(englishInt(12345678))
print(englishInt(1000000000))
print(englishInt(100000000))
print(englishInt(100000))
print(englishInt(1003003003))
print(englishInt(100007))
'''

'''
6:48
16.17 - max contiguous sum in an array of positive and negative integers
'''

def maxSum(arr):
    if len(arr) == 0:
        return 0
    max_at_i = arr[0]
    gm = arr[0]
    for i in range(1, len(arr)):
        max_at_i = max(max_at_i + arr[i], arr[i])
        gm = max(gm, max_at_i)
    return gm

'''
print("16.17 max sum test cases")
print(maxSum([2, -8, 3, -2, 4, -10]))
'''

'''
16.22 Langton's Ant
'''

def langtonsAnt(k):
    numRows = numCols = 1
    minRow = minCol = maxRow = maxCol = 0
    white = set()
    # 0 1 2 3 top right down left
    direction = 1
    currRow = currCol = 0
    initialK = k
    while k > 0:
        # determine which direction to go
        if (currRow, currCol) in white:
            direction = (direction + 1) % 4
            white.remove((currRow, currCol))
        else:
            direction -= 1
            if direction < 0:
                direction = 3
            # flip the current position before moving
            white.add((currRow, currCol))
        '''
        Move the ant. If the ant goes out of bounds, "slide the grid" to keep the ant's
        coordinates non-negative and all the positions the ant has touched to be non-negative. 
        The reason we want all positions to be non-negative, is because it is easier to construct
        the grid that way. So if the ant moves too far up for example, its row will be -1. In that case
        we must shift the grid up by 1, which essentially moves all positions DOWN by 1. For example, a 
        square that was initially at position (1, 2) (row, col) will now be at (2, 2) when the grid is shifted
        up by 1. The same thing applies for when the ant goes too far left, which is negative. 

        Another way to think about it is that the positions where the ant was/is are fixed in place, and you are "sliding"
        the grid in a particular direction behind them. All the positions after this sliding of the grid are now in new
        positions. 
        '''
        if direction == 0:
            currRow -= 1
            if currRow < minRow:
                minRow = currRow
                numRows += 1
        elif direction == 1:
            currCol += 1
            if currCol > maxCol:
                maxCol = currCol
                numCols += 1
        elif direction == 2:
            currRow += 1
            if currRow > maxRow:
                maxRow = currRow
                numRows += 1
        elif direction == 3:
            currCol -= 1
            if currCol < minCol:
                minCol = currCol
                numCols += 1
        k -= 1
    white = shiftDown(white, abs(minRow))
    white = shiftRight(white, abs(minCol))
    currRow += abs(minRow)
    currCol += abs(minCol)
    # '-' is black, '1' is white. we start with all black grid
    grid = [['-' for _ in range(numCols)] for _ in range(numRows)]
    for coordinate in white:
        r, c = coordinate
        grid[r][c] = '1'
    grid[currRow][currCol] = 'A'
    print("Langtons Ant for k = {0}".format(initialK))
    for row in grid:
        print(row)
    print('\n----------------------------------\n')

def shiftDown(s, shiftAmount) -> set:
    newWhite = set()
    for coordinate in s:
        row, col = coordinate
        newWhite.add((row + shiftAmount, col))
    return newWhite

def shiftRight(s, shiftAmount) -> set:
    newWhite = set()
    for coordinate in s:
        row, col = coordinate
        newWhite.add((row, col + shiftAmount))
    return newWhite

'''
for i in range(16):
    langtonsAnt(i)
'''



            







