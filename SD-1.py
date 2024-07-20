import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        
        # Configure background color
        self.root.configure(bg="powder blue")
        
        # Labels and Entry
        self.label_temp = tk.Label(root, text="Enter temperature:", bg="powder blue", font=("Comic Sans MS", 14))
        self.label_temp.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_temp = tk.Entry(root)
        self.entry_temp.grid(row=0, column=1, padx=10, pady=10)
        
        # Current unit label and OptionMenu
        self.label_from = tk.Label(root, text="Current unit:", bg="powder blue", font=("Comic Sans MS", 14))
        self.label_from.grid(row=1, column=0, padx=10, pady=10)
        
        self.from_var = tk.StringVar()
        self.from_var.set("Celsius")
        self.from_options = ["Celsius", "Fahrenheit", "Kelvin"]
        
        self.from_menu = tk.OptionMenu(root, self.from_var, *self.from_options)
        self.from_menu.config(bg="navy", fg="white", font=("Comic Sans MS", 12, "bold"))
        self.from_menu.grid(row=1, column=1, padx=10, pady=10)
        
        # Convert to label and OptionMenu
        self.label_to = tk.Label(root, text="Convert to:", bg="powder blue", font=("Comic Sans MS", 14))
        self.label_to.grid(row=2, column=0, padx=10, pady=10)
        
        self.to_var = tk.StringVar()
        self.to_var.set("Fahrenheit")
        self.to_options = ["Celsius", "Fahrenheit", "Kelvin"]
        
        self.to_menu = tk.OptionMenu(root, self.to_var, *self.to_options)
        self.to_menu.config(bg="navy", fg="white", font=("Comic Sans MS", 12, "bold"))
        self.to_menu.grid(row=2, column=1, padx=10, pady=10)
        
        # Convert button with navy blue background, white text, and playful font style
        button_font = tkFont.Font(family="Comic Sans MS", size=16, weight="bold")
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_temperature, bg="navy", fg="white", font=button_font)
        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Result label with powder blue background
        self.result_label = tk.Label(root, text="", bg="powder blue", font=("Comic Sans MS", 14))
        self.result_label.grid(row=4, columnspan=2, padx=10, pady=10)
    
    def convert_temperature(self):
        try:
            temperature = float(self.entry_temp.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()
            
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    result = f"{temperature:.2f}°C is converted to {temperature * 9 / 5 + 32:.2f}°F."
                elif to_unit == "Kelvin":
                    result = f"{temperature:.2f}°C is converted to {temperature + 273.15:.2f}K."
                else:
                    result = f"No conversion needed. Temperature remains {temperature:.2f}°C."
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    result = f"{temperature:.2f}°F is converted to {(temperature - 32) * 5 / 9:.2f}°C."
                elif to_unit == "Kelvin":
                    result = f"{temperature:.2f}°F is converted to {(temperature - 32) * 5 / 9 + 273.15:.2f}K."
                else:
                    result = f"No conversion needed. Temperature remains {temperature:.2f}°F."
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    result = f"{temperature:.2f}K is converted to {temperature - 273.15:.2f}°C."
                elif to_unit == "Fahrenheit":
                    result = f"{temperature:.2f}K is converted to {(temperature - 273.15) * 9 / 5 + 32:.2f}°F."
                else:
                    result = f"No conversion needed. Temperature remains {temperature:.2f}K."
            
            self.result_label.config(text=result)
        
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numerical value for temperature.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
