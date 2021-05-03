import serial
import struct
import win32ui

def rgba(colorref):
    mask = 0xff
    return [(colorref & (mask << (i * 8))) >> (i * 8) for i in range(4)]

ser = serial.Serial('COM3', 9600, timeout = 0)

while True:
    j = win32ui.FindWindow(None, "e2eSoft iVCam").GetWindowDC().GetPixel(300,200)
    r, g, b, a = rgba(j)
    win32ui.FindWindow(None, "e2eSoft iVCam").GetWindowDC().DeleteDC()
    ser.write(struct.pack("BBB", r, g, b))