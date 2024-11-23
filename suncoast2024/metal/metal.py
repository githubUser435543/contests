s = input()

def removePalindrome(rm, string, start, length):
    # include if not in palindrome range
    return "".join([string[i] for i in range(len(string)) if not (i >= start and i < start + length)]) 

oddPalindrome = False
cycleVowel = {"a":"e", "e":"i", "i":"o", "o":"u", "u":"a",}
vowels = "aeiou"
def foundPalindrome(a, b):
    c = sorted(b)
    if oddPalindrome:
        c = map(lambda x: x if x not in vowels else cycleVowel[x], c)
    print(a + "".join(c))
    exit(0)


palindrome = ""
rest = s

for palindromeSize in range(len(s), 0, -1):
    for offset in range(len(s) - palindromeSize + 1):
        # if odd palindrome size
        if palindromeSize % 2 == 1:
            # also remember slices are 0 indexed then 1 indexed
            leftEnd = offset + palindromeSize//2 + 1
            rightOffset = leftEnd - 1 # 1 -> 0 indexing
            rightEnd = rightOffset + palindromeSize // 2 + 1

            left = s[offset:leftEnd]
            right = s[rightOffset: rightEnd]
            if left == "".join(reversed(right)):
                palindrome = left + right[1:]
                oddPalindrome = True
                rest = removePalindrome(palindrome, s, offset, palindromeSize) 
                foundPalindrome(palindrome, rest)
        else:
            leftEnd = offset + palindromeSize//2
            rightOffset = leftEnd # remember, index change shifts this over
            rightEnd = rightOffset + palindromeSize//2

            left = s[offset:leftEnd]
            right = s[rightOffset:rightEnd]
            if (left == str(reversed(right))):
                palindrome = left + right
                rest = removePalindrome(palindrome, s, offset, palindromeSize)
                foundPalindrome(palindrome, rest)
                




foundPalindrome(palindrome, rest)




