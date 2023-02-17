from ceaser import get_char, is_letter
    
def key_str(msg, key):
    key_str=''
    key = key.lower()
    if len(msg)<=len(key):
        return key
    key_str=(key*int((len(msg)-(len(msg)%len(key)))/len(key)))+key[:(len(msg)%len(key))]
    for i in range(len(msg)):
        if is_letter(msg[i])==False:
            key_str = key_str[:i]+'-'+key_str[i:]
    return key_str
    
    
  
def vigenere(message, k):
    ks = key_str(message, k)
    fstr=''
    for c in range(len(message)):
        fstr += get_char(message[c], (ord(ks[c])-97))
    
    return fstr

print(vigenere('Meet me at the park at eleven am!', 'bacon'))
