def get_unique_elements(my_list):
    unique_list = []
    for element in my_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
