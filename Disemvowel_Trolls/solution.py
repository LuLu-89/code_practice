def disemvowel(string):
    vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
    for x in string:
        if x in vowel:
            string = string.replace(x, "")
    return string