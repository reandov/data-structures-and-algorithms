# Hash map declaration
hashMap = {}
print("Hashmap [init]:", hashMap)

# Adding items
hashMap["apples"] = 5
hashMap["oranges"] = 3
hashMap["grapes"] = 10
print("Hashmap [add]:", hashMap)

# Checking if element exists
print("Hashmap [access]:", hashMap.get("apples"))
print("Hashmap [access]:", hashMap.get("bananas"))

# Updating items
if ("apples" in hashMap):
    hashMap["apples"] = 15

if ("bananas" in hashMap):
    hashMap["bananas"] = 15
else:
    hashMap["bananas"] = 8

print("Hashmap [update]:", hashMap)

# Removing elements
hashMap.pop("grapes")

print("Hashmap [remove_target]:", hashMap)

hashMap.popitem()

print("Hashmap [remove_last]:", hashMap)

# Copying dict
hashMapCopy = hashMap.copy()
hashMapCopy["peach"] = 7
hashMap["watermelon"] = 17

print("Hashmap [original]", hashMap)
print("Hashmap [copy]", hashMapCopy)

# Clearing Hashmap
hashMap.clear()

print("Hashmap [clear]:", hashMap)