import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

random_array = np.arange(1,16) 
np.random.shuffle(random_array)
print(random_array)
plt.plot(random_array)
plt.title("Random Array")
plt.show()

def quicksort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[0]
  left = [i for i in arr[1:] if i <= pivot] 
  right = [i for i in arr[1:] if i > pivot]

  return quicksort(left) + [pivot] + quicksort(right)

sorted_array = quicksort(random_array)
print(sorted_array)

plt.plot(sorted_array)
plt.title("Sorted Array")
plt.show()
