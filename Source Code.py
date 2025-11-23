import tkinter as tk
from tkinter import messagebox, ttk

# FUNCTION: Calculate BMI

def calculate_bmi():
    try:
        weight = weight_var.get()
        height_cm = height_var.get()
        gender = gender_var.get()

        if gender == "":
            messagebox.showwarning("Warning", "Please select gender!")
            return

        height = height_cm / 100  # convert to meters

        bmi = round(weight / (height * height), 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
            color = "darkblue"
            advice = "Increase calorie intake with nutrient-dense foods, eat more protein-rich foods, nuts, dairy, banana shake and incorporate strength training"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            color = "green"
            advice = "Maintain your diet with portion control, stay hydrated and exercise regularly."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "red"
            advice = "Reduce sugar intake, increase pysical activity, walk daily, focus on a balanced diet with lean proteins, whole grains and vegetables."
        else:
            category = "Obese"
            color = "maroon"
            advice = "Consult a dietician, avoid junk food, adopt a healthy calorie controlled diet and increse physical activity."

        result_label.config(text=f"BMI : {bmi}\nCategory : {category}", fg=color)
        advice_label.config(text=f"Health Advice:\n{advice}", fg=color)

    except:
        messagebox.showerror("Error", "Something went wrong!")

# FUNCTION: Reset all fields

def reset():
    gender_var.set("")
    weight_var.set(50)
    height_var.set(160)
    result_label.config(text="")
    advice_label.config(text="")

# GUI SETUP

root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("500x600")
root.config(bg="#eef4ff")

title = tk.Label(root, text="BMI Calculator", font=("Britannic Bold", 34, "bold"), bg="#eef4ff")
title.pack(pady=20)

# GENDER SELECTION
gender_label = tk.Label(root, text="Select Gender:", font=("Bookman Old Style", 18), bg="#eef4ff")
gender_label.pack()

gender_var = tk.StringVar()

gender_frame = tk.Frame(root, bg="#eef4ff")
gender_frame.pack(pady=5)

male_rb = ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
female_rb = ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")

male_rb.grid(row=0, column=0, padx=10)
female_rb.grid(row=0, column=1, padx=10)

# HEIGHT SLIDER
height_label = tk.Label(root, text="Height (cm):", font=("Bookman Old Style", 14), bg="#eef4ff")
height_label.pack()

height_var = tk.DoubleVar(value=160)

height_scale = ttk.Scale(root, from_=100, to=220, orient="horizontal", variable=height_var, length=300)
height_scale.pack()

height_value = tk.Label(root, textvariable=height_var, bg="#eef4ff", font=("Bookman Old Style", 14))
height_value.pack(pady=5)

# WEIGHT SLIDER
weight_label = tk.Label(root, text="Weight (kg):", font=("Bookman Old Style", 14), bg="#eef4ff")
weight_label.pack()

weight_var = tk.DoubleVar(value=50)

weight_scale = ttk.Scale(root, from_=20, to=150, orient="horizontal", variable=weight_var, length=300)
weight_scale.pack()

weight_value = tk.Label(root, textvariable=weight_var, bg="#eef4ff", font=("Bookman Old Style", 14))
weight_value.pack(pady=5)

# CALCULATE BUTTON
calc_button = tk.Button(root, text="Calculate BMI", font=("Bookman Old Style", 20, "bold"),
                        bg="#142539", fg="white", width=15, height=1,
                        command=calculate_bmi)
calc_button.pack(pady=20)

# RESULT LABEL
result_label = tk.Label(root, text="", font=("Cambria", 16, "bold"), bg="#eef4ff")
result_label.pack(pady=10)

# ADVICE LABEL
advice_label = tk.Label(root, text="", font=("Cambria", 12), bg="#eef4ff", wraplength=400)
advice_label.pack(pady=10)

# RESET BUTTON
reset_btn = tk.Button(root, text="Reset", font=("Bookman Old Style", 14,"bold"),
                      bg="#a81a1a", fg="white", width=10, command=reset)
reset_btn.pack(pady=20)

root.mainloop()