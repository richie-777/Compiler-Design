def stateX(n):
    if (len(n) == 0):
        print("string not accepted")
    else:
        if (n[0] == 'a'):
            stateY(n[1:])
        elif (n[0] == 'b'):
            print("string not accepted")
def stateY(n):
    if (len(n) == 0):
        print("string not accepted")
    else:
        if (n[0] == 'a'):
            print("string not accepted")
        elif (n[0] == 'b'):
            stateZ(n[1:])
def stateZ(n):
    if (len(n) == 0):
        print("string accepted")
    else:
        if (n[0] == 'a'):
            stateZ(n[1:])
        elif (n[0] == 'b'):
            stateZ(n[1:])
n = input("Enter the string: ")
stateX(n)
