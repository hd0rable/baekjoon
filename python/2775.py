t=int(input())
for i in range(t):
  k=int(input())
  n=int(input())
  people = [i for i in range(1, n+1)] #0층

  for a in range(k):
    new=[]
    for b in range(1,n+1):
      new.append(sum(people[:b])) #아래층의 1~n호 까지의 합
    people=new.copy()
  print(people[-1]) #k층n호

# items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# items[2:5] # 인텍스 2에서 인덱스 5까지(인덱스 5는 제외) 슬라이싱 
# # [2, 3, 4]

# items[5:] # 인덱스 5에서 끝까지 슬라이싱
# # [5, 6, 7, 8, 9, 10]

# items[:3] # 처음부터 인덱스 3까지(인덱스 3은 제외) 슬라이싱 
# # [0, 1, 2]

# items[:] # 처음부터 끝까지 슬라이싱(즉, 리스트 복사본 반환)
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
