import tkinter as tk
from tkinter import messagebox

def cal_bmi():

    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100   # convert to meter
        bmi = weight / (height ** 2)
        display_bmi(bmi)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")


def display_bmi(bmi):
    if bmi < 18.5:
        result = f"BMI: {bmi:.2f} (Underweight)"
    elif 18.5 <= bmi < 24.9:
        result = f"BMI: {bmi:.2f} (Normal weight)"
    elif 25 <= bmi < 29.9:
        result = f"BMI: {bmi:.2f} (Overweight)"
    else:
        result = f"BMI: {bmi:.2f} (Obesity)"
    label_result.config(text=result)


root = tk.Tk()                  # create main window
root.title("BMI Calculator")

# create & place widgets
label_weight = tk.Label(root, text="weight (Kg):")
label_weight.grid(row=0, column=0, padx=10, pady=10)

entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(root, text="Height (cm):")
label_height.grid(row=1, column=0, padx=10, pady=10

entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

button_cal = tk.Button(root, text="Calculate BMI", command=cal_bmi)
button_cal.grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Button(root, text="BMI: ")
label_result.grid(row=3, column=0, pady=10)


root.mainloop()     # ending main window
