def fibonacci_series_recursive(n):
   if n ==0:
      return []
   elif n ==1:
      return[0]
   elif n ==2:
      return[0,1]
   else:
      fib_series=fibonacci_series_recursive(n-1)
      fib_series.append(fib_series[-1] + fib_series[-2])
      return fib_series
   
   
result=fibonacci_series_recursive(10)
print(result)