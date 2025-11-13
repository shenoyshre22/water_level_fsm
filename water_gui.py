import tkinter as tk
import time
import threading

# Simulated water levels (low, mid, high, motor_on, percentage)
levels = [
    (0, 0, 0, 1, "0%"),
    (1, 0, 0, 1, "25%"),
    (1, 1, 0, 1, "50%"),
    (1, 1, 1, 0, "70%"),
    (1, 1, 1, 0, "FULL")
]

root = tk.Tk()
root.title("Smart Water Control Simulation")

canvas = tk.Canvas(root, width=250, height=320, bg="lightblue")
canvas.pack(pady=10)

motor_label = tk.Label(root, text="Motor: OFF", font=("Arial", 14))
motor_label.pack(pady=5)

level_label = tk.Label(root, text="Water Level: 0%", font=("Arial", 14))
level_label.pack(pady=5)

# Draw tank function
def draw_tank(low, mid, high, motor_on, level_text):
    canvas.delete("all")
    canvas.create_rectangle(70, 50, 170, 270, outline="black", width=3, fill="white")

    # Fill water levels
    if low:
        canvas.create_rectangle(70, 220, 170, 270, fill="blue")
    if mid:
        canvas.create_rectangle(70, 170, 170, 220, fill="blue")
    if high:
        canvas.create_rectangle(70, 100, 170, 170, fill="blue")

    # Motor status
    motor_label.config(text=f"Motor: {'ON' if motor_on else 'OFF'}",
                       fg="green" if motor_on else "red")

    # Water level text
    level_label.config(text=f"Water Level: {level_text}")

# Animation function
def run_simulation():
    press_button.config(state="disabled")  # Disable the start button
    for (low, mid, high, motor_on, level_text) in levels:
        draw_tank(low, mid, high, motor_on, level_text)
        root.update()
        time.sleep(1.5)
    motor_label.config(text="Motor: OFF", fg="red")
    level_label.config(text="Water Level: FULL ✅")
    play_again_button.pack(pady=10)

# Threaded start to avoid freezing
def start_simulation():
    threading.Thread(target=run_simulation).start()

# Reset the GUI to play again
def reset_simulation():
    play_again_button.pack_forget()
    draw_tank(0, 0, 0, 0, "0%")
    press_button.config(state="normal")

# Start and replay buttons
press_button = tk.Button(root, text="Press", font=("Arial", 12, "bold"), bg="lightgreen", command=start_simulation)
press_button.pack(pady=15)

play_again_button = tk.Button(root, text="Wanna play it again?", font=("Arial", 12), bg="lightyellow", command=reset_simulation)

# Initial tank view
draw_tank(0, 0, 0, 0, "0%")

root.mainloop()
