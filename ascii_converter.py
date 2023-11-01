import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def convert_to_ascii():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        ascii_output = []
        
        for line in lines:
            try:
                decimal_value = int(line.strip())
                if 0 <= decimal_value <= 127:
                    ascii_value = chr(decimal_value)
                    ascii_output.append(ascii_value)
                else:
                    ascii_output.append(f"[Out of ASCII range: {decimal_value}]")
            except ValueError:
                ascii_output.append(f"[Invalid input: {line.strip()}]")
        
        result_label.config(text=f"ASCII: {''.join(ascii_output)}")
        
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Decimal to ASCII Converter from File")

# Create widgets
main_frame = ttk.Frame(root, padding="16")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

convert_button = ttk.Button(main_frame, text="Upload File & Convert", command=convert_to_ascii)
convert_button.grid(row=0, columnspan=2)

result_label = ttk.Label(main_frame, text="ASCII:", wraplength=400)
result_label.grid(row=1, columnspan=2, sticky=tk.W)

# Start the Tkinter event loop
root.mainloop()
