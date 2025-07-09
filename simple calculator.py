import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(root)
        input_frame.pack()

        input_field = tk.Entry(
            input_frame, font=("Arial", 18),
            textvariable=self.input_text, width=22,
            bd=8, relief=tk.RIDGE, justify="right"
        )
        input_field.pack(ipady=10)

        buttons_frame = tk.Frame(root)
        buttons_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                buttons_frame, text=text, width=10, height=3,
                command=lambda t=text: self.on_click(t)
            )
            if text == 'C':
                btn.grid(row=row, column=col, columnspan=4, sticky="nsew")
            else:
                btn.grid(row=row, column=col, sticky="nsew")

        for i in range(6):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.input_text.set(self.expression)
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("320x400")
    Calculator(root)
    root.mainloop()
