#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(nlogn) because n is being multiplied exponentially constantly


b) My best guess is O(logn), due to the fact that j is being multiplied by a constant amount


c) O(1), because the only decision here is whether or not bunnies is or is not 0, there's no iteration, just yes or no.

## Exercise II

## if i'm going in blind as to which floor will cause an egg break, I would likely use a binary_search of the floors
def binary_egg(building, n, f)
  start = building[0]
  end = building[n]
  midpoint = building[start] + building[n] // 2

# Likely if it's just an array, I would be ruling out floors by determining if floor f is hgiher or lower

  if start is less than end:
    if f == building[midpoint] (likely would use True or False):
      return building[midpoint]
    ## conditionals for determingi if f is higher or lower
    elif f < building[midpoint]:
      start = midpoint + 1
    elif f > building[midpoint]:
      end = midpoint - 1
  else:
    return start (because if we get down to the last element, it means that it has to be floor f)

## my best guess to the time complexity would be 0(logn), because we are dividing the array by a constant amount each iteration
