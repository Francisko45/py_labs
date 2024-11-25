import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Калькулятор")


entry = tk.Entry(root, font="Arial 20", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)


buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font="Arial 18", padx=20, pady=20)
        btn.grid(row=i+1, column=j, sticky="nsew")
        btn.bind("<Button-1>", on_click)


for i in range(5):  
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  
    root.grid_columnconfigure(j, weight=1)


root.mainloop()
