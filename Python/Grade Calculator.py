import tkinter as tk
import os

root = tk.Tk()

grades = []

count = int(input("\nHow many?"))
 
for i in range (count):
    grade = float(input("Enter A" + str(i + 1)+ ":"))
    if grade <= 0 or grade >= 100:
        print("incorret info")
    else:
        grades.append(grade)

avg = round((sum(grades)/count), 2)
ret = "Final Average :" + str(avg)

print(ret)

root.mainloop()

