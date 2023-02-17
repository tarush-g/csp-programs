def is_letter(char):
    if (65<=ord(char)<=90) or (97<=ord(char)<=122):
        return True
    else:
        return False

def get_char(char, key):
    if ord(char)<65 or 97>ord(char)>90 or ord(char)>122:
        return char
    if is_letter(char):
        if (((ord(char)+key) > 122) and char.islower()) or (((ord(char)+key) > 90) and char.isupper()):
            return chr((ord(char)+key)-26)
        return chr(ord(char)+key)
    
def caesar(msg, key):
    if key>26:
        key=key%26
    new_str=''
    for char in range(len(msg)):
        new_str+=get_char(msg[char], key)
    return new_str
    
