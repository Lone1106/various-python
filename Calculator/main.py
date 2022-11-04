# USES EVAL TO CALCULATE
import tkinter as tk


class Calculator():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("330x280")
        self.calculation = ""
        self.build_ui()
        self.root.mainloop()

    def add_to_field(self, symbol):
        self.calc_field.delete(1.0, "end")
        self.calculation += symbol
        self.calc_field.insert(1.0, self.calculation)

    def clear_field(self):
        self.calculation = ""
        self.calc_field.delete(1.0, "end")

    def calculate(self):
        final = eval(self.calculation)
        self.calc_field.delete(1.0, "end")
        self.calc_field.insert(1.0, final)

    def build_ui(self):
        self.button_one = tk.Button(
            text="1", width=5, height=2, command=lambda: self.add_to_field("1"))
        self.button_two = tk.Button(
            text="2", width=5, height=2, command=lambda: self.add_to_field("2"))
        self.button_three = tk.Button(
            text="3", width=5, height=2, command=lambda: self.add_to_field("3"))
        self.button_four = tk.Button(
            text="4", width=5, height=2, command=lambda: self.add_to_field("4"))
        self.button_five = tk.Button(
            text="5", width=5, height=2, command=lambda: self.add_to_field("5"))
        self.button_six = tk.Button(
            text="6", width=5, height=2, command=lambda: self.add_to_field("6"))
        self.button_seven = tk.Button(
            text="7", width=5, height=2, command=lambda: self.add_to_field("7"))
        self.button_eigth = tk.Button(
            text="8", width=5, height=2, command=lambda: self.add_to_field("8"))
        self.button_nine = tk.Button(
            text="9", width=5, height=2, command=lambda: self.add_to_field("9"))
        self.button_zero = tk.Button(
            text="0", width=5, height=2, command=lambda: self.add_to_field("0"))
        self.button_plus = tk.Button(
            text="+", width=5, height=2, command=lambda: self.add_to_field("+"))
        self.button_minus = tk.Button(
            text="-", width=5, height=2, command=lambda: self.add_to_field("-"))
        self.button_div = tk.Button(
            text="*", width=5, height=2, command=lambda: self.add_to_field("*"))
        self.button_mult = tk.Button(
            text="/", width=5, height=2, command=lambda: self.add_to_field("/"))
        self.button_clear = tk.Button(
            text="C", width=5, height=2, command=self.clear_field)
        self.button_calc = tk.Button(
            text="=", width=5, height=2, command=self.calculate)
        self.button_comma = tk.Button(
            text=".", width=5, height=2, command=lambda: self.add_to_field("."))
        self.button_bracket_left = tk.Button(
            text="(", height=2, width=5, command=lambda: self.add_to_field("("))
        self.button_bracket_right = tk.Button(
            text=")", height=2, width=5, command=lambda: self.add_to_field(")"))
        self.calc_field = tk.Text(height=4, width=46)

        self.button_one.grid(column=0, row=1)
        self.button_two.grid(column=1, row=1)
        self.button_three.grid(column=2, row=1)
        self.button_four.grid(column=0, row=2)
        self.button_five.grid(column=1, row=2)
        self.button_six.grid(column=2, row=2)
        self.button_seven.grid(column=0, row=3)
        self.button_eigth.grid(column=1, row=3)
        self.button_nine.grid(column=2, row=3)
        self.button_zero.grid(column=1, row=4)
        self.button_plus.grid(column=3, row=1)
        self.button_minus.grid(column=3, row=2)
        self.button_mult.grid(column=3, row=3)
        self.button_div.grid(column=3, row=4)
        self.button_clear.grid(column=0, row=4)
        self.button_calc.grid(column=2, row=4)
        self.button_comma.grid(column=0, row=5)
        self.button_bracket_left.grid(column=1, row=5)
        self.button_bracket_right.grid(column=2, row=5)
        self.calc_field.grid(column=0, row=0, columnspan=4)


if __name__ == "__main__":
    Calculator()
