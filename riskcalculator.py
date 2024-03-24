import tkinter as tk
from tkinter import messagebox

def calculate_diabetes_risk():
    
    try:
        # pregnancies_entry={}
        pregnancies = int(pregnancies_entry.get())
        glucose = float(glucose_entry.get())
        bp = float(bp_entry.get())
        skin_thickness = float(skin_thickness_entry.get())
        insulin = float(insulin_entry.get())
        bmi = float(bmi_entry.get())
        pedigree_function = float(pedigree_function_entry.get())
        age = int(age_entry.get())

        # Formula to calculate diabetes risk
        diabetes_risk = 0.021 * pregnancies + 0.332 * glucose + 0.217 * bp + \
                        0.072 * skin_thickness + 0.009 * insulin + \
                        0.226 * bmi + 0.147 * pedigree_function + 0.122 * age - 3.89

        if diabetes_risk > 0:
            messagebox.showinfo("Result", "You are at risk of diabetes!")
        else:
            messagebox.showinfo("Result", "You are not at risk of diabetes.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("Diabetes Risk Calculator")

# Labels
labels = ["Pregnancies:", "Glucose (mg/dL):", "Blood Pressure (mm Hg):", "Skin Thickness (mm):",
          "Insulin (mu U/ml):", "BMI:", "Pedigree Function:", "Age:"]
for i, label_text in enumerate(labels):
    tk.Label(root, text=label_text).grid(row=i, column=0, sticky="w")

# Entry fields
entry_fields = {}
for i, label_text in enumerate(labels):
    entry_fields[label_text] = tk.Entry(root)
    entry_fields[label_text].grid(row=i, column=1)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_diabetes_risk)
calculate_button.grid(row=len(labels), column=0, columnspan=2)

root.mainloop()
