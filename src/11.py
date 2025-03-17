def get_unique_elements(my_list):
    seen = set()
    return [x for x in my_list if x not in seen and not seen.add(x)]

my_list = ["apple", "banana", "cherry", "banana", "cherry"]
print(get_unique_elements(my_list))
