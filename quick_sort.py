def quick_sort(arr,low,high):
  if len(arr)<2:
    return arr
  else:
    if low<high:
      pi = partition(arr,low,high)
      quick_sort(arr,low,pi-1)
      quick_sort(arr,pi+1,high)
    return arr
      
def partition(arr,low,high):
  i = low-1
  pivot = arr[high]
  for j in range(low,high):
    if arr[j] <= pivot:
      i+=1
      arr[j],arr[i] = arr[i],arr[j]
      
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1

arr = [50,65,99,87,74,63,76,100]
print(quick_sort(arr,0,len(arr)-1))