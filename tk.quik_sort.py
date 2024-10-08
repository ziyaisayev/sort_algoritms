import tkinter as tk 
from tkinter import messagebox 


def pivot(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if pivot>=arr[j]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quik_sort(arr,low,high):
  if low<high:
      p=pivot(arr,low,high)
      quik_sort(arr, low, p-1)
      quik_sort(arr, p+1, high)


def sort_list(): 
    
    try: 
        input_list=list(map(int, entry.get().split(",")))
        sorted_list=quik_sort(input_list)
        result_label.config(text=f"Sorted list: {sorted_list}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please only add integers")

root=tk.Tk()
root.title(" quik Sort")

entry_label=tk.Label(root, text="Enter list (comma-separated): ")
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry=tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=10, pady=10)

sort_button=tk.Button(root, text="SORT", command=sort_list)
sort_button.grid(row=1, columnspan=2, padx=10, pady=10)

result_label=tk.Label(root, text="Sorted list: ")
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
