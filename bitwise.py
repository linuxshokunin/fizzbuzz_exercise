#!/usr/bin/python

for i in range(1,100):
  x = 0
  if i % 5 == 0:
    x += 1

  x <<=  1

  if i % 3 == 0:
    x +=  1

  if x == 1:
    print(i, x, "BUZ")
  elif x == 2:
    print(i, x, "FIZZ")
  elif x == 3:
    print(i, x, "FIZZBUZZ")
  else:
    print(i, x, i)
