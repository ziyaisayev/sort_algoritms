import tkinter as tk 
from tkinter import messagebox 


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
    return arr


def sort_list(): 
    
    try: 
        input_list=list(map(int, entry.get().split(",")))
        sorted_list=bubble_sort(input_list)
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
