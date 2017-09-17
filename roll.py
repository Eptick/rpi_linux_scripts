import random
s1 = 5
s2 = 3
def Roll():
    return random.randint(1,6)
def S1_Roll():
    if(s1 > 3):
        return [ Roll(), Roll(), Roll() ]
    elif(s1 == 3):
        return [ Roll(), Roll() ]
    else:
        return [ Roll() ]
def S2_Roll():
    if(s2 > 2):
        if(s1 < 3):
            return [ Roll() ]
        else:
            return [ Roll(), Roll() ]
    else:
        return [ Roll() ]
def Decide(s1_r, s2_r):
    global s1
    global s2
    print(s1_r, s2_r)
    if(len(s1_r) == 3):
        m = min(s1_r)
        for i in range(0, len(s1_r)):
            if(s1_r[i] == m):
                s1_r.pop(i)
                break
    if(len(s1_r) == 2 and len(s2_r) == 2):
        if( max(s1_r) > max(s2_r) ):
            s2 = s2 - 1
        else:
            s1 = s1 - 1
        if( min(s1_r) > min(s2_r) ):
            s2 = s2 - 1
        else:
            s1 = s1 - 1
    if(len(s1_r) == 2 and len (s2_r) == 1):
        if( max(s1_r) > max(s2_r) ):
            s2 = s2 - 1
        else:
            s1 = s1 - 1
    if(len(s1_r) == 1 and len (s2_r) == 1):
        if( max(s1_r) > max(s2_r) ):
            s2 = s2 - 1
        else:
            s1 = s1 - 1
while s1 > 1 and s2 > 0:          
    Decide(S1_Roll(), S2_Roll())
    print("S1: " + str(s1) + " S2: " + str(s2) )
        
