import tkinter as tk 
from tkinter import messagebox 


def insertion_sort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x
    return A


def sort_list(): 
    
    try: 
        input_list=list(map(int, entry.get().split(",")))
        sorted_list=insertion_sort(input_list)
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