import numpy as np

random_array = np.random.randint(1, 100, 15)
print(random_array)

def quicksort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[0]
  left = [i for i in arr[1:] if i <= pivot] 
  right = [i for i in arr[1:] if i > pivot]

  return quicksort(left) + [pivot] + quicksort(right)

sorted_array = quicksort(random_array)
print(sorted_array)
