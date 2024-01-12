# a,b,v=map(int,input().split())
# cnt=0
# goal=0
# while(True):
#   goal+=a
#   cnt+=1
#   if(goal>=v): #정상에 올라가면 미끄러지지않음.
#     break
#   goal-=b
# print(cnt)

#위에코드 런타임에러걸림 --> v값이 큰값이주어지면 계속돌려야해서;
#수학문제 방정식으로--> 규칙찾아서 간단히 해야함

# 달팽이는 낮에 나무막대에 다 올라갈 것
# 그럼 도달하는 날을 x일이라고 했을 때,
# 총 올라가는 횟수는 x, 내려오는 횟수는 (x-1)
# Ax - B(x-1) = V 가 될 것이고, 이를 x에 대한 식으로 정리한다면
# x = (V-B)/(A-B) 
# 이 x가 x의 정수형과 같다면, (즉, x가 나누어 떨어진다면)
# 달팽이는 x일에 다 올라갈 것
# 그렇지 않다면, 달팽이는 하루 더 지나서 나무막대에 다 올라갈 것

a,b,v=map(int,input().split())
goal=(v-b)/(a-b)
if goal == int(goal):
    print(int(goal))
else:
    print(int(goal) + 1)
