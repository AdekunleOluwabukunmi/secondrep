x = 1
if x ==1:
    print("hello")
    

class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r)


class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)


# https://d3c33hcgiwev3.cloudfront.net/-OMaFVMuRSGjGhVTLgUhfQ_69eef712625847d297a5740aa8ed8cf1_XubuntuCS.02.2022.PVG.MOOC.zip?Expires=1654819200&Signature=cKnjEy2GQmVtWedDxRBtVmPIqpi30umIqQlCrQ8Tem64UN8THH69VdGahPLD7ggNj2uMwrSVblWKOelfa02UPSLuLFkCzkFkVU-4l80RgEaeSy0-90lE1JZaTQktsCArbXhcWcxMjJpD75zGf2VMAeLU~MBj4DgJk8bT4RlMEGI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

#metaclass

class Test:
    pass
print(type(Test))
Test = type('Test', (), {})
gos = 'something'


b = int(input('Enter an integer >'))
print(abs(b))
print(b)


# def find_missing_side(first_side, first_length, second_side, second_length):
#     if first_side == 'AB':
#         return 'AC', int((first_length ** 2 + second_length ** 2) ** 0.5)
#     elif first_side == 'BC':
#         return 'AC', int((first_length ** 2 + second_length ** 2) ** 0.5)
#     else:
#         return 'AB', int((first_length ** 2 - second_length ** 2) ** 0.5)

# def main():
#     while True:
#         first_segment = input("Enter first segment: ")
#         first_length = int(input("Enter first Length: "))
#         second_segment = input("Enter second segment: ")
#         second_length = int(input("Enter second Length: "))

#         missing_side, missing_length = find_missing_side(first_segment, first_length, second_segment, second_length)
#         print(f"The missing side is {missing_side} with length {missing_length}.\n")

#         option = input("Do you want to continue? (yes/no): ").lower()
#         if option != 'yes':
#             break

# if __name__ == "__main__":
#     main()

frist_len= "AB"
second_len = "BC"
# third_seg = "AC"

print("Don't forget segment AB = 1st, BC = 2nd, AC= 3rd")
def looking_for_missing_side_of_bobby_dick(first, first_len, second_s, second_len):
    if first == 'AB':
        return 'AC', int((first_len ** 2 + second_len ** 2) ** 0.5)
    elif first == 'BC':
        return 'AC', int((first_len ** 2 + second_len ** 2) ** 0.5)
    else:
        return 'AB', int((first_len ** 2 - second_len ** 2) ** 0.5)

def main():
    while True:
        first_seg = input("Enter your first segement: ")
        first_len= int(input("Enter first Length: "))
        second_seg = input("Enter second segment: ")
        second_len = int(input("Enter second Length: "))

        missing_sid, missing_leng = looking_for_missing_side_of_bobby_dick(first_seg, first_len, second_seg, second_len)
        print(f"The missing side is {missing_sid} with length {missing_leng}.\n")

        runmore = input("Repeat for AB, BC, or AC? (yes/no)").lower()
        if runmore != 'yes':
            break

if __name__ == "__main__":
    main()
