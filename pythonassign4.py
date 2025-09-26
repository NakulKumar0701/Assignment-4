try:
    b = input("Enter file name : ")
    a = open(b, "r")
    x = a.readline()
    y = a.readline()
    print("Reading file content:")
    print("Line1 :", x.strip())
    print("Line2 :", y.strip())
except FileNotFoundError:

    print(f"The file {b} was not found")    







