import keyboard
from pynput.mouse import Listener, Button
import tkinter as tk

root=tk.Tk()

# specify size of window.
root.geometry("300x170")
root.wm_title("Message Paster")
 
# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)
 
# Create label
l = tk.Label(root, text = "Click mouse wheel to paste")
l.config(font =("Courier", 12))
 
Fact = """AnatomyOfDeath is recruiting. We are an international guild offering a friendly environment for PvE and PvP players. If you're interested, feel free to whisper!"""

def click(x,y,button,pressed):
    if pressed and button == Button.middle:
        message = T.get("1.0", "end-1c")
        print(message)
        keyboard.write(message)

listener = None
        
def enable():
    if b1["state"] == tk.NORMAL and b2["state"] == tk.DISABLED:
        print("enable clicked")
        global listener
        listener = Listener(on_click=click)
        listener.start()
        b1["state"] = tk.DISABLED
        b2["state"] = tk.NORMAL

def disable():
    if b1["state"] == tk.DISABLED and b2["state"] == tk.NORMAL:
        print("disable clicked")
        listener.stop()
        b1["state"] = tk.NORMAL
        b2["state"] = tk.DISABLED
        
# Create button to activate.
b1 = tk.Button(root, text = "Activate", command=enable)
 
# Create the stop button.
b2 = tk.Button(root, text = "Stop", command = disable, state=tk.DISABLED)
 
l.pack()
T.pack()
b1.pack()
b2.pack()
 
# Insert The Fact.
T.insert(tk.END, Fact)
 
tk.mainloop()
