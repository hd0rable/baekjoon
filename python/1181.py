import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
  arr.append(sys.stdin.readline().strip())
arr=list(set(arr)) #중복제거
arr.sort() #사전순으로 정렬
arr.sort(key=len) #길이짧은 순
for i in arr:
  print(i)

  #반복입력이 많은 문제에서는 sys.stdin.readline()이 확실히 빠루다!!
  #sys로 입력받을때 공백제거 .strip() 이거 해줘야댐ㅁ
