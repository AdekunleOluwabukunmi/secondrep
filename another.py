def find_missing_side(first_side, first_length, second_side, second_length):
    if first_side == 'AB':
        return 'AC', int((first_length ** 2 + second_length ** 2) ** 0.5)
    elif first_side == 'BC':
        return 'AC', int((first_length ** 2 + second_length ** 2) ** 0.5)
    else:
        return 'AB', int((first_length ** 2 - second_length ** 2) ** 0.5)

def main():
    while True:
        first_segment = input("Enter first segment: ")
        first_length = int(input("Enter first Length: "))
        second_segment = input("Enter second segment: ")
        second_length = int(input("Enter second Length: "))

        missing_side, missing_length = find_missing_side(first_segment, first_length, second_segment, second_length)
        print(f"The missing side is {missing_side} with length {missing_length}.\n")
        option = input("Do you want to continue? (yes/no): ").lower()
        if option != 'yes':
            break

if __name__ == "__main__":
    main()

