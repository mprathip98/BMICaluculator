from customtkinter import *
window = CTk()
window.title("BMI Calculator")
window.geometry("500x650")
window.resizable(False, False)
set_appearance_mode("dark")
from tkinter import messagebox

measureChoice = False

def measure(choice):
    global measureChoice
    if choice == 'Metric':
        weightLabel.configure(text="Weight (kg) : ")
        window.update()
        heightLabel.configure(text="Height (cm) : ")
        window.update()
        measureChoice = True
    elif choice == "English":
        weightLabel.configure(text="Weight (lb) : ")
        window.update()
        heightLabel.configure(text="Height (in) : ")
        window.update()
        measureChoice = False


def calculate():
    try:
        weight = int(weightEntry.get())
        height = int(heightEntry.get())
        if not measureChoice:
            total = int(weight)/(int(height)**2)*703
            resultLabel.configure(text=f"You BMI is = {str(float(round(total)))}")
            if total < 18.5:
                descpLabel.configure(text="UNDERWEIGHT", text_color="blue")
            elif 18.5 < total < 25:
                descpLabel.configure(text="Normal", text_color="green")
            elif 25 < total < 30:
                descpLabel.configure(text="Overweight", text_color="red")
            else:
                descpLabel.configure(text="OBESE", text_color="purple")
        if measureChoice:
            total = (weight/height)/height*10000
            resultLabel.configure(text=f"You BMI is = {str(float(round(total)))}")
            if total < 18.5:
                descpLabel.configure(text="UNDERWEIGHT", text_color="blue")
            elif 18.5 < total < 25:
                descpLabel.configure(text="Normal", text_color="green")
            elif 25 < total < 30:
                descpLabel.configure(text="Overweight", text_color="red")
            else:
                descpLabel.configure(text="OBESE", text_color="purple")


    except:
        messagebox.showerror(title="An error has occurred", message="Try again and enter only numbers")





titleLabel = CTkLabel(master=window, text="BMI Calculator", font=("Impact", 40), text_color='skyBlue')
titleLabel.place(x=135, y=20)

dropDown = CTkComboBox(master=window,
                       values=["English", 'Metric'],
                       height=25,
                       width=100,
                       corner_radius=10,
                       fg_color='black',
                       text_color='skyBlue',
                       font=('Impact', 12),
                       command=measure
                       )
dropDown.place(x=200, y=90)

weightLabel = CTkLabel(master=window, text=" Weight (lb) : ", font=("Impact", 25))
weightLabel.place(x=110, y=160)

weightEntry = CTkEntry(master=window, corner_radius=10, fg_color='black', text_color='skyBlue', font=('Impact', 23))
weightEntry.place(x=245, y=160)

heightLabel = CTkLabel(master=window, text=" Height (in) : ", font=("Impact", 25))
heightLabel.place(x=110, y=220)

heightEntry = CTkEntry(master=window, corner_radius=10, fg_color='black', text_color='skyBlue', font=('Impact', 23))
heightEntry.place(x=245, y=220)

submitButton = CTkButton(master=window,
                         corner_radius=10,
                         fg_color='black',
                         text_color='skyBlue',
                         text="Calculate",
                         width=160,
                         height=55,
                         font=("Impact", 29),
                         command=calculate)
submitButton.place(x=170, y=300)

resultLabel = CTkLabel(master=window, text=" ", font=("Impact", 35), text_color='skyBlue')
resultLabel.place(x=125, y=400)
descpLabel = CTkLabel(master=window, text=" ", font=("Impact", 25), text_color='blue')
descpLabel.place(x=175, y=450)

window.mainloop()