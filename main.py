import time

#subroutine  to time the execution of bubbleSort()
def time_bubbleSort(array):
  start_time = time.time()
  
  bubbleSort(array)
  
  end_time = time.time()
  print("Time taken for bubbleSort: ", end_time - start_time)



#bubble sort algorthim
def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
          
  return arr

arr = [1,2,3,4,5,6,7,8,9,10]
result =  bubbleSort(arr)
print(result)
print(time_bubbleSort(arr))