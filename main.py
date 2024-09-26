import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Old Digital Clock")

# Function to update the time with a flipping effect
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Get current time
    for i, (new, old) in enumerate(zip(current_time, label["text"])):
        if new != old:
            # Update only the changed part to simulate flipping
            flip_animation(i, new)
    label.after(1000, update_time)  # Call again after 1 second

def flip_animation(index, new_char):
    current_text = label["text"]
    # Temporarily blank out the changing digit
    new_text = current_text[:index] + ' ' + current_text[index + 1:]
    label.config(text=new_text)
    root.after(150, lambda: finalize_flip(index, new_char))  # Delay the actual change

def finalize_flip(index, new_char):
    current_text = label["text"]
    # Set the new digit in place after a brief pause
    new_text = current_text[:index] + new_char + current_text[index + 1:]
    label.config(text=new_text)

# Create a label to display the time, initially blank
label = tk.Label(root, font=('Courier', 50), background='black', foreground='green')
label.pack(anchor='center')
label.config(text=" " * 11)  # Initial blank space for time (e.g., HH:MM:SS AM/PM)

# Start the clock
update_time()

# Run the application
root.mainloop()
