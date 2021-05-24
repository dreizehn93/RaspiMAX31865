import tkinter as tk
from tkinter.font import BOLD
import board
import digitalio
import adafruit_max31865

# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
#sensor = adafruit_max31865.MAX31865(spi, cs)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=4, filter_frequency=50)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create label
        self.ueberschrift=tk.Label(text="Temperatur [°C]")
        self.ueberschrift.config(font=("Arial",20), bg="darkred", fg="red")
        self.ueberschrift.pack()
        self.l = tk.Label(text = "Temperatur")
        self.l.config(font =("Arial bold", 240), bg="darkred", fg="red")
        self.l.pack()
        
        self.quit = tk.Button(self, text="QUIT", bg="darkred", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
        # initial timer start
        self.onUpdate()

    def onUpdate(self):
        #update displayed time
        # Read temperature.
        temp = sensor.temperature
        # Print the value.
        self.l.config(text="{0:0.1f}".format(temp))
        print("Temperature: {0:0.3f}C".format(temp))
        # call myself after 1 second
        self.after(1000, self.onUpdate)

root = tk.Tk()
root.geometry("1000x400")
root.configure(bg="darkred")
app = Application(master=root)
app.mainloop()