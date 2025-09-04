def merge_sort(arr):
  if len(arr)<2:
    return arr
  else:
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)
    
def merge(left,right):
  i=j=0
  sorted_arr = []
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      sorted_arr.append(left[i])
      i+=1
    else:
      sorted_arr.append(right[j])
      j+=1
      
  sorted_arr.extend(left[i:])
  sorted_arr.extend(right[j:])
  return sorted_arr

arr = [50,65,99,87,74,63,76,100]
print(merge_sort(arr))