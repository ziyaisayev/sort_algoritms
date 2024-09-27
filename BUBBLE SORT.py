def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n):
        swapped=False
        
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
        
list1=[2,5,3,8,4,9,1]
print(list1)
bubble_sort(list1)
print(list1)

