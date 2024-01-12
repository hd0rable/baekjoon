# n=int(input())
# arr=[]
# for i in range(n):
#   arr.append(int(input()))
# arr.sort()
# for i in range(n):
#   print(arr[i])

# 이 문제는 메모리 제한이 너무 적어서 sort를 사용할 수 없다.
# 게다가 for문에서 숫자를 입력 받기 위해 input을 사용해도 메모리 초과로 문제를 통과할 수 없다.

# 따라서 sort를 쓰지 않고, intput 대신 int(sys.stdin.readline()) 이 함수를 쓰는것이 이 문제의 핵심이다.

#이문제는 계수정렬이용 -->>
# 카운트 할 배열을 선언하고, 정렬할 배열 요소가 몇개가 있는지 카운트 배열 각 인덱스에 담는다. 
####데이터의 크기가 한정되어  빠르게 동작해야할 때 사용된다.####

import sys
n=int(sys.stdin.readline())
arr=[0] * (10000 + 1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언
for i in range(n):
  num=int(sys.stdin.readline())
  arr[num]+=1
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):# arr[num]에 num이 들어온 개수 만큼 출력 
            print(i)
