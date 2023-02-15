def user_input():
    try:
        a0 = int(input("Enter first progression member: "))
        d = int(input("Enter difference between neighbour progression members: "))
        n = int(input("Enter quantity of progression members:"))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Incorrect number!")
        return user_input()
    return a0, d, n


a0, d, n = user_input()
for i in range(n):
    print(a0 + i * d)
