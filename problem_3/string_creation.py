
def creation(input_string, strings): 
    size = len(input_string)
    if size == 0:
        return True

    for i in range(size+1):
        if input_string[:i] in strings and creation(input_string[i:], strings):
            return True
    return False

strings = ["front", "back", "end", "yard", "pain"]
print(creation("backend", strings))