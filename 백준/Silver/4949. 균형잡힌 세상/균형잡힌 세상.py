string=input()
while(string!='.'):
     stack=[]
     i=0
     for char in string:
          if char=='(' or char=='[':
               stack.append(char)
          elif char==')' or char==']':
               if not stack:
                    print('no')
                    break
               elif (char==']' and stack[-1]=='[') or (char==')' and stack[-1]=='('):
                    del stack[-1]
               else:
                    print('no')
                    break
          elif char=='.':
               if not stack:  print('yes')
               else:          print('no')
     string=input()