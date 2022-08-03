def start(c):
    if (c == 'a'):
        dfa = 1
    elif (c == 'b'):
        dfa = 3
    else:
        dfa = -1
    return dfa
def state1(c):
    if (c == 'a'):
        dfa = 2
    elif (c == 'b'):
        dfa = 4
    else:
        dfa = -1
    return dfa
# dfa = state of DFA
def state2(c):
    if (c == 'b'):
        dfa = 3
    elif (c == 'a'):
        dfa = 1
    else:
        dfa = -1
    return dfa
def state3(c):
    if (c == 'b'):
        dfa = 3
    elif (c == 'a'):
        dfa = 4
    else:
        dfa = -1
    return dfa
def state4(c):
    dfa = -1
    return dfa
def isAccepted(String):
    l = len(String)
    dfa = 0
    for i in range(l):
        if (dfa == 0):
            dfa = start(String[i])
        elif (dfa == 1):
            dfa = state1(String[i])
        elif (dfa == 2):
            dfa = state2(String[i])
        elif (dfa == 3):
            dfa = state3(String[i])
        elif (dfa == 4):
            dfa = state4(String[i])
        else:
            return 0
    if (dfa == 3):
        return 1
    else:
        return 0
if __name__ == "__main__":
    String = "aaaaaabbbb"
    if (isAccepted(String)):
        print("ACCEPTED")
    else:
        print("NOT ACCEPTED")