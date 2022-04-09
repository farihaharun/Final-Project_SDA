import cv2
from matplotlib import pyplot as plt
from tkinter import filedialog
from tkinter import messagebox

try:
    img = cv2.imread(filedialog.askopenfilename(), -1)
    cv2.imshow('Image:', img)

    color = ('b', 'g', 'r')
    Blue = 0
    Green = 0
    Red = 0
    totalPixel = 0

    for channel, col in enumerate(color):
        histogram = cv2.calcHist([img], [channel], None, [256], [1, 256])
        plt.plot(histogram, color=col)
        plt.xlim([0, 256])
        totalPixel += sum(histogram)
        # print(histogram)
        if channel == 0:
            Blue = sum(histogram)
        elif channel == 1:
            Green = sum(histogram)
        elif channel == 2:
            Red = sum(histogram)

    Blue = (Blue / totalPixel) * 100
    Green = (Green / totalPixel) * 100
    Red = (Red / totalPixel) * 100


    def printc(r, g, b):
        plt.title("Red: " + str(r) + "%; Green: " + str(g) + "%; Blue: " + str(b) + "%")


    def con(x):
        if x < 20:
            messagebox.showinfo("Suggestion ", "Location is suitable for industrial planning")
        else:
            messagebox.showinfo("Suggestion: ", "Location is not suitable for industrial planning")


    printc(Red, Green, Blue)
    plt.show()
    con(Red)


except:
    messagebox.showinfo("Error", "Please select an image file!")
