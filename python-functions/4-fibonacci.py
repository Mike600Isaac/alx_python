def fibonacci_sequence(n):
  if n <= 0:
    return []
  elif n == 1:
    return [1]
  elif n == 2:
    return [0,1]
  fib_sequence = [0,1]
  while (len(fib_sequence) < n):
    next_numb = fib_sequence(-1) + fib_sequence(-2)
    fibonacci_sequence(next_numb)
  return fib_sequence