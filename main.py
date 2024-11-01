fruit_tuple = ("Apple", "Banana", "Cherry", "Date")
print(fruit_tuple[0])
print(fruit_tuple[3])

slice_tuple = fruit_tuple[1:3]
print(slice_tuple)

num_tuple = (3, 5, 3, 2, 8, 3, 7)
print(num_tuple.count(3))
print(num_tuple.index(8))

person_info = ("Alice", 28, "Engineer")
name, age, job = person_info
print(name)
print(age)
print(job)