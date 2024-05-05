# insert data at specific location
data = [1, 2, 3, 4, 5]
index = 2
item = "new_data"
print(data)
data.insert(index, item)
print(data)

# delete data
data = [1, 2, 3, 4, 5]
index = 2
item = "new_data"
print(data)

data.insert(index, item)

print(data)

item_to_remove = 3
if item_to_remove in data:
    data.remove(item_to_remove)

print(data)

# Count the total number of occurrences of any word in a list
data = ["apple", "banana", "apple", "orange", "apple", "grapes"]
word_to_count = "apple"

word_count = data.count(word_to_count)
print(f"Total occurrences of '{word_to_count}' in the list: {word_count}")

name = ['akshay', 'meet', 'rahul', 'krishna']
age = [20, 30, 25, 21, 18]

name.pop(2)
# name.remove('rahul')
print(name)

age.sort()
print(age)

name.append("Artist")
print(name)

age.insert(2,25)
print(age)

print(age.count(25))

print(name)
print(len(name))
print(age)
print(len(age))