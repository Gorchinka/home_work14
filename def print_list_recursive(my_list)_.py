def print_list_recursive(my_list):
    if my_list:
        print(my_list[0])
        return print_list_recursive(my_list[1:])
    else:
        print("End of list")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list_recursive(my_list)