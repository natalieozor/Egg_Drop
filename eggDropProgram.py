import math

def drop():
    Hw = float(raw_input("Mr. Wright's height (m): "))
    Hb = float(raw_input("Building height (m): "))
    V = float(raw_input("Mr. Wright's velocity (m/s): "))
    X = float(raw_input("Mr. Wright's horizontal distance away (m): "))
    tEgg =(1-(math.sqrt(39.2*(Hb-Hw)))/-9.8)
    tWright = X / V
    tWait = tWright - tEgg
    #tTest = tWait + tEgg #this value is the total time that seconds are being counted. it SHOULD equal tWright --> collision
    #return tWait, tEgg, tWright, tTest #testing to see if all the values work
    return tWait

print("Wait " + str(drop()) + " seconds.")
