import tkinter as tk
import time

# Simulated states (replace with parsed VCD if needed)
levels = [
    (0, 0, 0, 1),  # Empty - motor on
    (1, 0, 0, 1),  # Low
    (1, 1, 0, 1),  # Mid
    (1, 1, 1, 0),  # Full - motor off
    (1, 0, 0, 1),
    (0, 0, 0, 1)
]

root = tk.Tk()
root.title("Smart Water Control FSM Simulation")

canvas = tk.Canvas(root, width=300, height=400, bg="lightblue")
canvas.pack()

# Tank outline
canvas.create_rectangle(100, 50, 200, 350, outline="black", width=3)
motor_text = canvas.create_text(150, 30, text="Motor: OFF", font=("Arial", 14))

water = canvas.create_rectangle(100, 350, 200, 350, fill="blue", outline="")

def animate():
    for low, mid, high, motor in levels:
        # Determine water height
        height = 0
        if low: height = 100
        if mid: height = 200
        if high: height = 300

        # Update water level
        canvas.coords(water, 100, 350 - height, 200, 350)

        # Update motor status
        status = "ON" if motor else "OFF"
        color = "green" if motor else "red"
        canvas.itemconfig(motor_text, text=f"Motor: {status}", fill=color)

        root.update()
        time.sleep(1)

animate()
root.mainloop()
