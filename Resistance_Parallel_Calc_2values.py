import tkinter as tk

# --- functions ---
#---GUI for adding two resistors in parallel and in series
# Future project with be with 3 or more resistors
# Would also like to make a reverse calculation which give parallel resistor for ohm value desired
def generate():
    try:
        con1 = (1 / float(num1.get())) # seems to work better if done in steps
        con2 = (1 / float(num2.get())) # con is for conductance
        consum = con1 + con2       
        result = 1/consum
        result2 = float(num1.get()) + float(num2.get()) #using float is obvious way
    except Exception as ex: 
        print(ex)
        result = 'error'

    num3.set(result)
    num4.set(result2)

# --- main ---

root = tk.Tk()

num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
num4 = tk.StringVar()
tk.Label(root, text=" Input R1:").grid(row=0, column=0)
tk.Label(root, text="Input R2:").grid(row=1, column=0)
tk.Label(root, text=" Output Parallel:").grid(row=2, column=0)
tk.Label(root, text="Output Series:").grid(row=3, column=0)

tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)
tk.Entry(root, textvariable=num3).grid(row=2, column=1)
tk.Entry(root, textvariable=num4).grid(row=3, column=1)
button = tk.Button(root, text="Calculate", command=generate)
button.grid(row=4, column=1)

root.mainloop()