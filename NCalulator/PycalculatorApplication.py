import customtkinter as ctk
import Arithmeticcal as a
import TDcalculator as td
import currencyconverter as cc
import unitconverter as uc
import TRDcalculator as trd
import pyttsx3
ctk.set_appearance_mode("Light")  # Options: "Light", "Dark", "System"


def toggle_mode():
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Light":
        ctk.set_appearance_mode("Dark")
        btn_toggle.configure(text="☀️")
    else:
        ctk.set_appearance_mode("Light")
        btn_toggle.configure(text="🌙")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def on_click():
    speak("Welcome to the multi functional calculator application This application contains two dimensional calculator, three dimensional calculator, and unit converter This calculator performs basic operations like addition, subtraction, multiplication, and division This calculator is used to find area and perimeter of basic two dimensional shapes It includes square, rectangle, triangle, and circle This calculator is used to find volume and surface area of three dimensional shapes It includes cube, cuboid, sphere, and cylinder This application is used to convert Indian rupees into different foreign currencies It supports conversion to US dollars, euros, British pounds, and other currencies This application is used to convert Indian rupees into different foreign currencies It supports conversion to US dollars, euros, British pounds, and other currencies")
    

        
top=ctk.CTk()
top.geometry("1500x1000")
top.title("Main Page")
La=ctk.CTkLabel(top,text="NCALCULATOR",font=("Arial",25))
La.place(x=50,y=65)
btn1=ctk.CTkButton(top,text="Arithmetic Calculator",fg_color="blue",hover_color="green",command=a.arithmetic)
btn1.place(x=30,y=150)
btn2=ctk.CTkButton(top,text="2D CALCULATOR",fg_color="blue",hover_color="green",command=td.tdcalc)
btn2.place(x=30,y=190)
btn3=ctk.CTkButton(top,text="currency converter",fg_color="blue",hover_color="green",command=cc.currencycon)
btn3.place(x=30,y=230)
btn4=ctk.CTkButton(top,text="Unit converter",fg_color="blue",hover_color="green",command=uc.unitconverter)
btn4.place(x=30,y=270)
btn5=ctk.CTkButton(top,text="3D CALCULATOR",fg_color="blue",hover_color="green",command=trd.threedcalc)
btn5.place(x=30,y=310)
btn6=ctk.CTkButton(top,text="About the Calculator?",fg_color="blue",hover_color="green",command=on_click)
btn6.place(x=30,y=350)
btn_toggle = ctk.CTkButton(top, text="🌙", command=toggle_mode)
btn_toggle.place(x=190,y=150)
top.mainloop()
