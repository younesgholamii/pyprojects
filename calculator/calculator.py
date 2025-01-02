from tkinter import Tk, Entry, Button, StringVar
from sympy import sympify, sqrt, sin, cos, tan, pi

def convert_to_radians(expression):
    if 'sin(' in expression or 'cos(' in expression or 'tan(' in expression:
        expression = expression.replace('sin(', 'sin(pi/180*')
        expression = expression.replace('cos(', 'cos(pi/180*')
        expression = expression.replace('tan(', 'tan(pi/180*')
    return expression


class Calculator:
    
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("400x600")
        master.config(bg='gray')
        master.resizable(True, True)

        self.equation = StringVar()
        self.entry_value = ''
        
        Entry(
            master, bg="#1e1e1e", fg="white", font=("Arial Bold", 30),
            textvariable=self.equation, justify="left"
        ).grid(row=0, column=0, columnspan=5, sticky="nsew", ipadx=8, ipady=15)

        buttons = [
            ('sin', 1, 0, "orange", "black"), ('(', 1, 1, "orange", "black"), (')', 1, 2, "orange", "black"), ('%', 1, 3, "orange", "black"), ('/', 1, 4, "orange", "black"),
            ('cos', 2, 0, "orange", "black"), ('7', 2, 1, "white", "black"), ('8', 2, 2, "white", "black"), ('9', 2, 3, "white", "black"), ('*', 2, 4, "orange", "black"),
            ('tan', 3, 0, "orange", "black"), ('4', 3, 1, "white", "black"), ('5', 3, 2, "white", "black"), ('6', 3, 3, "white", "black"), ('-', 3, 4, "orange", "black"),
            ('√', 4, 0, "orange", "black"), ('1', 4, 1, "white", "black"), ('2', 4, 2, "white", "black"), ('3', 4, 3, "white", "black"), ('+', 4, 4, "orange", "black"),
            ('^', 5, 0, "orange", "black"), ('C', 5, 1, "orange", "black"), ('0', 5, 2, "white", "black"), ('.', 5, 3, "orange", "black"), ('=', 5, 4, "black", "orange"),
        ]

        for (text, row, col, fgcolor, bgcolor) in buttons:
            Button(
                master, text=text, bg=bgcolor, fg=fgcolor, font=("Arial", 22),
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(8):
            master.grid_rowconfigure(i, weight=1)
        for j in range(5):
            master.grid_columnconfigure(j, weight=1)

    def on_button_click(self, value):
        if value == 'C':
            self.clear()
        elif value == '=':
            self.solve()
        elif value == '√':
            self.show('sqrt(')
        elif value == '^':
            self.show('**')
        elif value in ['sin', 'cos', 'tan']:
            self.show(value + '(')
        else:
            self.show(value)

    def show(self, value):
        if value in "+-*/%.**":
            if self.entry_value and self.entry_value[-1] in "+-*/%.**":
                return  
            if not self.entry_value and value in "+-*/%":
                return  
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            expression = convert_to_radians(self.entry_value)
            result = sympify(expression).evalf()
            result = round(result, 4)
            self.entry_value = str(result)
            self.equation.set(result)
        except ZeroDivisionError:
            self.equation.set("تقسیم بر صفر غیرمجاز است")
            self.entry_value = ''
        except Exception:
            self.equation.set("خطا")
            self.entry_value = ''


root = Tk()
calculator = Calculator(root)
root.mainloop()
