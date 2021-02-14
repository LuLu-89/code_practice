def get_count(input_str):
    num_vowel = 0
    for vowel in input_str:
        if vowel in 'aeiou':
            num_vowel += 1
    
    return num_vowel