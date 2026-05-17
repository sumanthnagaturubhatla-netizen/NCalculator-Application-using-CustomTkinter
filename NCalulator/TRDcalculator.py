import customtkinter as ctk
import cube as cu
import cubiod as cb
import sphere as sp
import cylinder as cy

def threedcalc():
    top = ctk.CTk()
    top.configure(bg_color="lightblue")   # background color
    top.geometry("500x450")
    top.title("3D Calculator")

    tdla = ctk.CTkLabel(top, text="THREE DIMENSIONAL CALCULATOR", font=("Arial", 25))
    tdla.place(x=40, y=65)

    btn1 = ctk.CTkButton(top, text="Cube Calculator",
                         fg_color="green", hover_color="blue",
                         command=cu.cube)
    btn1.place(x=60, y=130)

    btn2 = ctk.CTkButton(top, text="Cuboid Calculator",
                         fg_color="green", hover_color="blue",
                         command=cb.cuboid)
    btn2.place(x=60, y=190)

    btn3 = ctk.CTkButton(top, text="Sphere Calculator",
                         fg_color="green", hover_color="blue",
                         command=sp.sphere)
    btn3.place(x=60, y=250)

    btn4 = ctk.CTkButton(top, text="Cylinder Calculator",
                         fg_color="green", hover_color="blue",
                         command=cy.cylinder)
    btn4.place(x=60, y=310)

    top.mainloop()