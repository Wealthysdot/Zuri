# register
# login

# Dictionary
# created using curly {} KeyValue pairs

# List, this is just an example of list
# aSampleList = [1, 2, 3, 4, 5]

# method 1 adding value to the dictionary

dictionaryOne = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',

}

# method2
dictionaryTwo = {}
dictionaryTwo['key4'] = 'value4'
dictionaryTwo['key5'] = 'value5'
dictionaryTwo['key6'] = 'value5'

# to delete from a dictionary
# del dictionaryTwo['key4']
#
# dictionaryOne.pop('key1')
# print(dictionaryOne)

# print(aSampleList)

# How to loop through the item in a dictionary
for key, value in dictionaryOne.items():
    print(" I have " + key + "relating with " + value)
