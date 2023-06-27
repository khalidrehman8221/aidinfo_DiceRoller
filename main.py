import random
import tkinter as tk

def roll_dice(num_dice):
    """Rolls the specified number of dice and returns the results as a list."""
    results = []
    for _ in range(num_dice):
        result = random.randint(1, 6)
        results.append(result)
    return results

def roll_button_click():
    """Event handler for the Roll button click."""
    num_dice = int(num_dice_entry.get())
    results = roll_dice(num_dice)
    result_label.config(text="Results: " + ", ".join(str(result) for result in results))

def quit_button_click():
    """Event handler for the Quit button click."""
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Create and configure the widgets
num_dice_label = tk.Label(root, text="Number of dice:")
num_dice_entry = tk.Entry(root)
roll_button = tk.Button(root, text="Roll", command=roll_button_click)
result_label = tk.Label(root, text="Results:")
quit_button = tk.Button(root, text="Quit", command=quit_button_click)

# Arrange the widgets in the grid
num_dice_label.grid(row=0, column=0, padx=5, pady=5)
num_dice_entry.grid(row=0, column=1, padx=5, pady=5)
roll_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
quit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()
