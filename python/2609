a,b=map(int,input().split())
#유클리드 호제법 최대공약수 구하기
def GCD(a,b):
  while(b): #b가 참일 동안== 자연수일 때 == a%b!=0
    a,b=b,a%b
  return a
gcd=GCD(a,b)
print(gcd)
print(int((a*b)/gcd))

# #내장함수로 바로 구할수있음
# import math
# print(math.gcd(a,b)) #최대공약수
# print(math.lcm(a,b)) #최소공배수
