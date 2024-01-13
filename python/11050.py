n,k=map(int,input().split())

def f(n):
  ans=1
  for i in range(2,n+1):
    ans*=i
  return ans

def binomial(n,k):
  return f(n)//(f(k)*f(n-k))

print(binomial(n,k))

#https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
#https://velog.io/@newdana01/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%ED%95%AD%EA%B3%84%EC%88%98%EB%9E%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B5%AC%ED%98%84
