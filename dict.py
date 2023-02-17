def mapAB(dictionary):
    if "a" in dictionary and "b" in dictionary:
        dictionary["ab"] = dictionary["a"] + dictionary["b"]
    return dictionary

dict1 = {"a":"Hi", "b":"There"}
print(mapAB(dict1))
