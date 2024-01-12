n=int(input())
score=list(map(int,input().split()))
maxscore=max(score)
for i in range(n):
  score[i]=score[i]/maxscore*100
avg=sum(score)/n
print(avg)
