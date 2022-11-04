#USES EVAL TO CALCULATE
import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("330x280")

calculation = ""


def add_to_field(symbol):
    global calculation
    calc_field.delete(1.0, "end")
    calculation += symbol
    calc_field.insert(1.0, calculation)


def clear_field():
    global calculation
    calculation = ""
    calc_field.delete(1.0, "end")


def calculate():
    final = eval(calculation)
    calc_field.delete(1.0, "end")
    calc_field.insert(1.0, final)


button_one = tk.Button(
    text="1", width=5, height=2, command=lambda: add_to_field("1"))
button_two = tk.Button(
    text="2", width=5, height=2, command=lambda: add_to_field("2"))
button_three = tk.Button(
    text="3", width=5, height=2, command=lambda: add_to_field("3"))
button_four = tk.Button(
    text="4", width=5, height=2, command=lambda: add_to_field("4"))
button_five = tk.Button(
    text="5", width=5, height=2, command=lambda: add_to_field("5"))
button_six = tk.Button(
    text="6", width=5, height=2, command=lambda: add_to_field("6"))
button_seven = tk.Button(
    text="7", width=5, height=2, command=lambda: add_to_field("7"))
button_eigth = tk.Button(
    text="8", width=5, height=2, command=lambda: add_to_field("8"))
button_nine = tk.Button(
    text="9", width=5, height=2, command=lambda: add_to_field("9"))
button_zero = tk.Button(
    text="0", width=5, height=2, command=lambda: add_to_field("0"))
button_plus = tk.Button(
    text="+", width=5, height=2, command=lambda: add_to_field("+"))
button_minus = tk.Button(
    text="-", width=5, height=2, command=lambda: add_to_field("-"))
button_div = tk.Button(
    text="*", width=5, height=2, command=lambda: add_to_field("*"))
button_mult = tk.Button(
    text="/", width=5, height=2, command=lambda: add_to_field("/"))
button_clear = tk.Button(
    text="C", width=5, height=2, command=clear_field)
button_calc = tk.Button(
    text="=", width=5, height=2, command=calculate)
button_comma = tk.Button(
    text=".", width=5, height=2, command=lambda: add_to_field("."))
button_bracket_left = tk.Button(
    text="(", height=2, width=5, command=lambda: add_to_field("("))
button_bracket_right = tk.Button(
    text=")", height=2, width=5, command=lambda: add_to_field(")"))

button_one.grid(column=0, row=1)
button_two.grid(column=1, row=1)
button_three.grid(column=2, row=1)
button_four.grid(column=0, row=2)
button_five.grid(column=1, row=2)
button_six.grid(column=2, row=2)
button_seven.grid(column=0, row=3)
button_eigth.grid(column=1, row=3)
button_nine.grid(column=2, row=3)
button_zero.grid(column=1, row=4)
button_plus.grid(column=3, row=1)
button_minus.grid(column=3, row=2)
button_mult.grid(column=3, row=3)
button_div.grid(column=3, row=4)
button_clear.grid(column=0, row=4)
button_calc.grid(column=2, row=4)
button_comma.grid(column=0, row=5)
button_bracket_left.grid(column=1, row=5)
button_bracket_right.grid(column=2, row=5)

calc_field = tk.Text(height=4, width=46)
calc_field.grid(column=0, row=0, columnspan=4)

window.mainloop()
