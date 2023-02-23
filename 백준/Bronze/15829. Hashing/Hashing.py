input()
string=input()
i=0
hashNum=0

for char in string:
     hashNum+=(ord(char)-96)*(31**i)
     i+=1
     
print(hashNum%1234567891)