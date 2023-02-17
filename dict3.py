def topping3(dict1):
    if "potato" in dict1:
        dict1["fries"] = dict1["potato"]
    if "salad" in dict1:
        dict1["spinach"] = dict1["salad"]
    return dict1


dict1 = {"potato": "ketchup", "salad": "oil"}
print(topping3(dict1))
