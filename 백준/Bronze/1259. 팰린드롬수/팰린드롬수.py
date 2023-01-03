while (True):
    s=input()
    if (s=='0'): break
    length=len(s)
    palindrome='yes'

    for i in range(length//2+1):
        if(s[i]==s[length-i-1]):
            continue
        else:
            palindrome='no'
            break
        
    print(palindrome)