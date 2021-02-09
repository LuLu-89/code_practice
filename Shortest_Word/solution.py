def find_short(s):
    shortest_length = 99
    for word in s.split():
        current_length = 0
        for letter in word:
            current_length += 1
        if current_length < shortest_length:
            shortest_length = current_length
    return shortest_length