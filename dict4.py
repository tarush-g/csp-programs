def mapAB4(dict1):
    if len(dict1["a"]) > len(dict1["b"]):
        dict1["c"] = dict1["a"]
    if len(dict1["a"]) < len(dict1["b"]):
        dict1["c"] = dict1["b"]
    if len(dict1["a"]) == len(dict1["b"]):
        dict1["a"] = ""
        dict1["b"] = ""
    return dict1

dict1 = {"a": "aa", "b":"bbb", "c": "cake"}
print(mapAB4(dict1))
            
            
