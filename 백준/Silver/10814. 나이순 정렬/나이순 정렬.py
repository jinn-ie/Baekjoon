import sys
input=sys.stdin.readline

judge=[]    # dict는 중복값 처리 불가

n=int(input())

for i in range(n):
    person=list(input().rstrip().split())
    judge.append(person)

s_judge=sorted(judge,key=lambda x:int(x[0]))
# int로 비교 안하면 9>10이 됨

for age,name in s_judge:
    print(age,name)