import customtkinter as ctk
import circle as cr
import Rectangle as re
import square as sq
import Triangle as tr

def tdcalc():
    top = ctk.CTk()
    top.configure(bg_color="lightblue")   # background color
    top.geometry("500x450")
    top.title("2D Calculator")

    tdla = ctk.CTkLabel(top, text="TWO DIMENSIONAL CALCULATOR", font=("Arial", 25))
    tdla.place(x=60, y=65)

    btn1 = ctk.CTkButton(top, text="Square Calculator",
                         fg_color="green", hover_color="blue",
                         command=sq.square)
    btn1.place(x=60, y=130)

    btn2 = ctk.CTkButton(top, text="Rectangle Calculator",
                         fg_color="green", hover_color="blue",
                         command=re.rectangle)
    btn2.place(x=60, y=190)

    btn3 = ctk.CTkButton(top, text="Triangle Calculator",
                         fg_color="green", hover_color="blue",
                         command=tr.triangle)
    btn3.place(x=60, y=250)

    btn4 = ctk.CTkButton(top, text="Circle Calculator",
                         fg_color="green", hover_color="blue",
                         command=cr.circle)
    btn4.place(x=60, y=310)
    
    

    top.mainloop()
