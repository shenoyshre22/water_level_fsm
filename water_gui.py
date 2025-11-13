import tkinter as tk
import time
import threading

# levels: (percentage, motor_on)
# motor_on = 1 => motor running (filling), 0 => motor off
levels = [
    (0, 1),    # 0%  - motor on (start filling)
    (25, 1),   # 25% - motor on
    (50, 1),   # 50% - motor on
    (75, 1),   # 75% - motor on
    (100, 0)   # 100% - full, motor off
]

root = tk.Tk()
root.title("Smart Water Control Simulation")

WIDTH = 300
HEIGHT = 420
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#e6f2ff")
canvas.pack(padx=10, pady=8)

# Labels
motor_label = tk.Label(root, text="Motor: OFF", font=("Arial", 14))
motor_label.pack(pady=(4,2))

level_label = tk.Label(root, text="Water Level: 0%", font=("Arial", 14))
level_label.pack(pady=(0,8))

# Play/retry buttons (created here, packed later)
def on_press():
    # spawn thread so UI doesn't freeze
    threading.Thread(target=run_simulation, daemon=True).start()

press_button = tk.Button(root, text="Press", font=("Arial", 12, "bold"),
                         bg="lightgreen", width=15, command=on_press)

play_again_button = tk.Button(root, text="Wanna play it again?", font=("Arial", 12),
                              bg="lightyellow", width=20)

# Tank geometry (centered)
tank_left = 90
tank_right = WIDTH - 90
tank_top = 60
tank_bottom = HEIGHT - 80
tank_height = tank_bottom - tank_top

# draw tank frame once
def draw_tank_frame():
    canvas.delete("frame")
    canvas.create_rectangle(tank_left, tank_top, tank_right, tank_bottom,
                            outline="black", width=3, fill="white", tags="frame")
    # tick marks / percent labels along side
    for p in (0, 25, 50, 75, 100):
        y = tank_bottom - (p / 100.0) * tank_height
        canvas.create_line(tank_right + 6, y, tank_right + 18, y, tags="frame")
        canvas.create_text(tank_right + 40, y, text=f"{p}%", anchor="w", font=("Arial", 9), tags="frame")

# Draw water according to percentage (0-100) and motor status
def draw_water(percent, motor_on):
    # remove previous water shapes
    canvas.delete("water")
    # compute fill top y
    fill_height = (percent / 100.0) * tank_height
    y_top = tank_bottom - fill_height
    # ensure full cover when 100
    canvas.create_rectangle(tank_left + 2, y_top, tank_right - 2, tank_bottom - 2,
                            fill="deepskyblue", outline="", tags="water")
    # small waves (optional)
    if percent >= 10:
        canvas.create_oval(tank_left + 10, y_top - 6, tank_left + 40, y_top + 6, fill="blue", outline="", tags="water")
        canvas.create_oval(tank_right - 40, y_top - 6, tank_right - 10, y_top + 6, fill="blue", outline="", tags="water")

    # motor label
    motor_label.config(text=f"Motor: {'ON' if motor_on else 'OFF'}", fg="green" if motor_on else "red")
    level_label.config(text=f"Water Level: {percent}%")

# simulation run (runs in background thread)
def run_simulation():
    # disable start button while running
    press_button.config(state="disabled")
    play_again_button.pack_forget()
    # animate through levels
    for (pct, motor) in levels:
        # animate smooth rising from current to next (optional)
        current_text = level_label.cget("text")
        # get numeric current percent if shown, else 0
        try:
            cur_pct = int(current_text.split(":")[1].strip().replace("%", ""))
        except Exception:
            cur_pct = 0
        step = 1 if pct >= cur_pct else -1
        for p in range(cur_pct, pct + step, step):
            draw_water(p, motor if p < pct else motor)  # keep motor as given; final state for that step
            root.update()
            time.sleep(0.02)  # smooth step
        # small pause at each milestone
        time.sleep(0.45)
    # final state: when FULL ensure motor_off
    draw_water(100, 0)
    root.update()
    # show replay button
    play_again_button.pack(pady=12)
    press_button.config(state="normal")

def reset_simulation():
    # hide replay, set to initial empt y
    play_again_button.pack_forget()
    draw_water(0, 1)   # 0% and motor on
    root.update()

# bind play again
play_again_button.config(command=reset_simulation)

# initial UI layout
draw_tank_frame()
draw_water(0, 1)    # show 0% initially with motor on
press_button.pack(pady=10)

root.mainloop()
