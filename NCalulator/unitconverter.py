import customtkinter as ctk
import lengthconversion as lc
import weightconversion as wc
import Temperatureconversion as tc
import litreconversion as llc

def unitconverter():
        top = ctk.CTk()
        top.geometry("1500x1000")
        top.title("Unit Converter")

        la1 = ctk.CTkLabel(top, text="Unit converter", font=("Arial",25))
        la1.place(x=30, y=50)

        btn1 = ctk.CTkButton(top, text="length conversion",
                             fg_color="green", hover_color="blue",
                             command=lc.lengthcon)
        btn1.place(x=30, y=100)

        btn2 = ctk.CTkButton(top, text="weight conversion",
                             fg_color="green", hover_color="blue",
                             command=wc.weightcon)
        btn2.place(x=30, y=190)

        btn3 = ctk.CTkButton(top, text="Temperature conversion",
                             fg_color="green", hover_color="blue",
                             command=tc.tempcon)
        btn3.place(x=30, y=280)

        btn4 = ctk.CTkButton(top, text="Litre conversion",
                             fg_color="green", hover_color="blue",
                             command=llc.litrecon)
        btn4.place(x=30, y=340)

        top.mainloop()