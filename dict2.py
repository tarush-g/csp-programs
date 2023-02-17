def topping1(dictionary):
    if "ice cream" in dictionary:
        dictionary["ice cream"] = "cherry"
    dictionary["bread"] = "butter"
    return dictionary

dict1 = {}
print(topping1(dict1))
