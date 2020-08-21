# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

## if i'm going in blind as to which floor will cause an egg break, I would likely use a binary_search of the floors
def binary_egg(building, n, f)
  start = building[0]
  end = building[n]
  midpoint = building[start] + building[n] // 2

# Likely if it's just an array, I would be ruling out floors by determining if floor f is hgiher or lower

  if start is less than end:
    if f == building[midpoint] (likely would use True or False):
      return building[midpoint]
    elif f < building[midpoint]:
      start = midpoint + 1
    elif f > building[midpoint]:
      end = midpoint - 1
  else:
    return start (because if we get down to the last element, it means that it has to be floor f)

## my best guess to the time complexity would be 0(logn), because we are dividing the array by a constant amount each iteration
    
