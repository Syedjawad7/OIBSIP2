import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter


def calculate_bmi(weight_kg, height_m):
    bmi = float(weight_kg / (height_m**2))
    return bmi


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def get_compliment(bmi_class):
    if bmi_class == "Underweight":
        return "It's important to ensure you are getting enough nutrients. Consult with a healthcare professional for guidance."
    elif bmi_class == "Normal weight":
        return "Congratulations! You are maintaining a healthy weight."
    elif bmi_class == "Obese":
        return "It's advisable to consult with a healthcare professional to discuss your weight management."
    else:
        return ""


def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        weight_unit = weight_unit_var.get()
        height_unit = height_unit_var.get()

        # Convert weight and height to kilograms and meters, respectively
        if weight_unit == "Pounds":
            weight = weight * 0.453592  # Convert pounds to kilograms
        if height_unit == "Centimeters":
            height = height / 100  # Convert centimeters to meters

        bmi_value = calculate_bmi(weight, height)
        bmi_class = interpret_bmi(bmi_value)
        compliment = get_compliment(bmi_class)
        result_text = f"Your BMI is: {bmi_value:.2f}\nClass: {bmi_class}"
        if compliment:
            result_text += f"\nCompliment: {compliment}"

        result_label.config(text=result_text)
    except ValueError:
        result_label.config(
            text="Please enter valid numerical values for weight and height."
        )


def resize_background(event):
    new_width = event.width
    new_height = event.height
    resized_image = original_background_image.resize((new_width, new_height))
    blurred_image = resized_image.filter(ImageFilter.GaussianBlur(radius=3))
    new_background_photo = ImageTk.PhotoImage(blurred_image)
    background_label.config(
        image=new_background_photo, width=new_width, height=new_height
    )
    background_label.image = (
        new_background_photo  # Keep a reference to avoid garbage collection
    )


# Create the main window
root = tk.Tk()
root.title("Bmi Calculator")

# Set the window size
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Color scheme
bg_color = "#ffffff"  # Green color with full opacity
text_color = "black"
button_color = "green"  # Green button

root.configure(bg=bg_color)

# Icon
img_icon = ImageTk.PhotoImage(file="C:\\Users\\DELL\\oibsip2\\OIBSIP2\\bg.png")
root.iconphoto(False, img_icon)

# Load original background image
original_background_image = Image.open("C:\\Users\\DELL\\oibsip2\\OIBSIP2\\bg.png")
original_background_photo = ImageTk.PhotoImage(original_background_image)

# Create background label
background_label = tk.Label(
    root, image=original_background_photo, width=window_width, height=window_height
)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place BMI calculator widgets on top of the background
height_label = ttk.Label(
    root, text="Height:", background=bg_color, foreground=text_color
)
height_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

height_entry = ttk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)

# Height unit dropdown
height_units = ["Meters", "Centimeters"]
height_unit_var = tk.StringVar(value=height_units[0])
height_unit_dropdown = ttk.Combobox(
    root, textvariable=height_unit_var, values=height_units, state="readonly"
)
height_unit_dropdown.grid(row=0, column=2, padx=10, pady=10)

weight_label = ttk.Label(
    root, text="Weight:", background=bg_color, foreground=text_color
)
weight_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")

weight_entry = ttk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# Weight unit dropdown
weight_units = ["Kilograms", "Pounds"]
weight_unit_var = tk.StringVar(value=weight_units[0])
weight_unit_dropdown = ttk.Combobox(
    root, textvariable=weight_unit_var, values=weight_units, state="readonly"
)
weight_unit_dropdown.grid(row=1, column=2, padx=10, pady=10)

# Bind the window resize event to the resize_background function
root.bind("<Configure>", resize_background)

# Create a custom style for the button
style = ttk.Style()
style.configure("TButton", background=button_color)

calculate_button = ttk.Button(
    root, text="Calculate BMI", command=calculate_button_clicked, style="TButton"
)
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

result_label = ttk.Label(root, text="Result")
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()
