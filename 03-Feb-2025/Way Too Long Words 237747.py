# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

t=int(input())
for i in range(t):
    st=input()
    if len(st) <= 10:
        print(st)
    else:
        print(st[0]+ str((len(st)-2))+st[-1])