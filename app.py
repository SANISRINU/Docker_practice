import tkinter as tk

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b if b != 0 else "Cannot divide by zero"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Enter valid numbers!")

app = tk.Tk()
app.title("My Calculator")
app.geometry("350x350")

tk.Label(app, text="Python Calculator",
         font=("Arial", 20, "bold")).pack(pady=15)

entry1 = tk.Entry(app, font=("Arial", 14))
entry1.pack(pady=5)

entry2 = tk.Entry(app, font=("Arial", 14))
entry2.pack(pady=5)

for op in ["+", "-", "*", "/"]:
    tk.Button(
        app,
        text=op,
        font=("Arial", 14),
        command=lambda x=op: calculate(x)
    ).pack(pady=3)

result_label = tk.Label(app, text="Result:",
                        font=("Arial", 16))
result_label.pack(pady=15)

app.mainloop()
