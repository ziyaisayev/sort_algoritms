import tkinter as tk 
from tkinter import messagebox 


def selection_sort(list1):
    for i in range(len(list1)):
        min_index = i
        for j in range(i+1, len(list1)):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i] , list1[min_index]=list1[min_index], list1[i]
        
    return list1


def sort_list(): 
    
    try: 
        input_list=list(map(int, entry.get().split(",")))
        sorted_list=selection_sort(input_list)
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
