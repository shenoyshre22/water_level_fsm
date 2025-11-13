**Smart Water Level Controller**

A Digital Design Project using Verilog + Python GUI Visualization

📘 **Overview**

This project simulates a Smart Water Level Controller System that automatically turns a motor ON or OFF based on water tank levels — implemented using Verilog (FSM design) and visualized using a Tkinter-based GUI in Python.

The Verilog module models the hardware logic of the controller, while the Python GUI provides a real-time visualization of how the water fills up and how the motor responds.

⚙️ **Features**

Verilog FSM to model the water level control system

Detects LOW, MID, and HIGH water levels

Automatically controls motor ON/OFF states

Simulated waveform viewing using GTKWave

Interactive Python GUI for live tank animation

Replay/reset option to rerun the simulation

🧩 **Project Structure**
Smart-Water-Level-Controller/
│

├── water_level_fsm/

│   ├── main.v                 # Verilog main design (FSM)

│   ├── tb.v                   # Verilog testbench

│   ├── water_level.vcd        # Generated waveform file

│

├── gui/

│   ├── water_gui.py           # Python Tkinter visualization

│
├── README.md                  # Project documentation

└── .gitignore

💡 **Working Principle**

The water level is divided into three zones:

Sensor	Description	Motor Action
LOW	Tank empty or low water level	Motor ON
MID	Water half full	Motor ON
HIGH	Tank full	Motor OFF

The FSM (Finite State Machine) transitions between:

EMPTY → FILLING → FULL

When FULL → Motor turns OFF

When water drops below HIGH → Motor turns ON again

🧠 **Verilog Files**
main.v

Implements the FSM logic:

module water_level_controller (
    input wire clk, reset,
    input wire low, mid, high,
    output reg motor_on
);

tb.v

Testbench to apply simulated signals for low, mid, and high sensors.
Generates a .vcd file for waveform visualization.

🧪 **Simulation Instructions**
1. Compile the Verilog files

Open your terminal inside the water_level_fsm/ folder and run:

iverilog -o water_level.out main.v tb.v

2. Run the simulation
vvp water_level.out


This will create a file called water_level.vcd.

3. View the waveform
gtkwave water_level.vcd


You can now observe low, mid, high, and motor_on waveforms to verify the FSM.

💻 **Python GUI Visualization**
1. Navigate to the gui folder
cd gui

2. Run the GUI
python water_gui.py

3. Usage

Click the “Press” button to start the simulation.

The tank will fill from 0% → 25% → 50% → 75% → 100%.

The Motor indicator shows:

🟢 “ON” while filling

🔴 “OFF” once the tank is full

After completion, click “Wanna play it again?” to restart.

🧰 **Tools & Technologies**

Icarus Verilog (iverilog) – Verilog compiler

GTKWave – Waveform viewer

Python 3 + Tkinter – GUI development

VS Code / ModelSim / Terminal – IDE and environment
