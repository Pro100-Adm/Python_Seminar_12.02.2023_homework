def user_input():
    try:
        min_number = int(input("Enter start list index value: "))
        max_number = int(input("Enter end list index value: "))
    except ValueError:
        print("Incorrect number!")
        return user_input()
    return min_number, max_number

min_number, max_number = user_input()
my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        print(i)