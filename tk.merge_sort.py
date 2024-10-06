import tkinter as tk 
from tkinter import messagebox 


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sort_list(): 
    
    try: 
        input_list=list(map(int, entry.get().split(",")))
        sorted_list=mergeSort(input_list)
        result_label.config(text=f"Sorted list: {sorted_list}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please only add integers")

root=tk.Tk()
root.title("Selection Sort")

entry_label=tk.Label(root, text="Enter list (comma-separated): ")
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry=tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=10, pady=10)

sort_button=tk.Button(root, text="SORT", command=sort_list)
sort_button.grid(row=1, columnspan=2, padx=10, pady=10)

result_label=tk.Label(root, text="Sorted list: ")
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()


