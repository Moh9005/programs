s=input("Enter the String = ")
if(len(s)==2):
    if ((s[0]=='S' and s[1]=='P') or (s[0]=='P' and s[1]=='S')):
        print("S is winner")
    elif ((s[0]=='P' and s[1]=='R') or (s[0]=='R' and s[1]=='P')):
        print("P is winner")
    elif ((s[0]=='R' and s[1]=='S') or (s[0]=='S' and s[1]=='R')):
        print("R is winner")
    else:
        print("DRAw")
else:
    Print("Invalid Input")