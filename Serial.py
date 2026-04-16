# import serial
import tkinter as tk

# ser = serial.Serial('COM3', 9600)

# def update_data():
#     if ser.in_waiting:
#         data = ser.readline().decode().strip()
#         label.config(text=data)
#     root.after(500, update_data)

root = tk.Tk()
root.title("Arduino Data")

label = tk.Label(root, text="Waiting...", font=("Arial", 20))
label.pack()

# update_data()
root.mainloop()