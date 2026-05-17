import customtkinter as ctk
import math

def arithmetic():
    def Add():
        a = int(e1.get())
        b = int(e2.get())
        c = a + b
        label_result.configure(text=f"Result: {c}")

    def sub():
        a = int(e1.get())
        b = int(e2.get())
        c = a - b
        label_result.configure(text=f"Result: {c}")

    def pro():
        a = int(e1.get())
        b = int(e2.get())
        c = a * b
        label_result.configure(text=f"Result: {c}")

    def mod():
        a = int(e1.get())
        b = int(e2.get())
        c = a % b
        label_result.configure(text=f"Result: {c}")

    def exp():
        a = int(e1.get())
        b = int(e2.get())
        c = a ** b
        label_result.configure(text=f"Result: {c}")

    def sin():
        a = int(e1.get())
        c = math.sin(a)
        label_result.configure(text=f"Result: {c}")

    def cos():
        a = int(e1.get())
        c = math.cos(a)
        label_result.configure(text=f"Result: {c}")

    def tan():
        a = int(e1.get())
        c = math.tan(a)
        label_result.configure(text=f"Result: {c}")

    def floordiv():
        a = int(e1.get())
        b = int(e2.get())
        c = a // b
        label_result.configure(text=f"Result: {c}")

    def log():
        a = int(e1.get())
        c = math.log(a)
        label_result.configure(text=f"Result: {c}")

    def div():
        a = int(e1.get())
        b = int(e2.get())
        c = a / b
        label_result.configure(text=f"Result: {c}")

    def fact():
        a = int(e1.get())
        fact = math.factorial(a)
        label_result.configure(text=f"Result: {fact}")

    # Main window
    top = ctk.CTk()
    top.geometry("500x450")
    #top.configure(bg_color="lightblue")
    top.title("Arithmetic Calculator")

    FirstNumber = ctk.CTkLabel(top, text="Enter the first Number:", font=("Arial", 15))
    FirstNumber.place(x=30, y=40)

    SecondNumber = ctk.CTkLabel(top, text="Enter the second Number:", font=("Arial", 15))
    SecondNumber.place(x=30, y=90)

    # Buttons with consistent styling
    addbtn = ctk.CTkButton(top, text="+", width=30, fg_color="green", hover_color="blue", command=Add)
    addbtn.place(x=30, y=150)

    subbtn = ctk.CTkButton(top, text="-", width=30, fg_color="green", hover_color="blue", command=sub)
    subbtn.place(x=70, y=150)

    Probtn = ctk.CTkButton(top, text="*", width=30, fg_color="green", hover_color="blue", command=pro)
    Probtn.place(x=110, y=150)

    modbtn = ctk.CTkButton(top, text="%", width=40, fg_color="green", hover_color="blue", command=mod)
    modbtn.place(x=30, y=180)

    expobtn = ctk.CTkButton(top, text="exp", width=40, fg_color="green", hover_color="blue", command=exp)
    expobtn.place(x=80, y=180)

    sinbtn = ctk.CTkButton(top, text="sin", width=40, fg_color="green", hover_color="blue", command=sin)
    sinbtn.place(x=130, y=180)

    cosbtn = ctk.CTkButton(top, text="cos", width=40, fg_color="green", hover_color="blue", command=cos)
    cosbtn.place(x=30, y=220)

    tanbtn = ctk.CTkButton(top, text="tan", width=40, fg_color="green", hover_color="blue", command=tan)
    tanbtn.place(x=80, y=220)

    floordivbtn = ctk.CTkButton(top, text="//", width=40, fg_color="green", hover_color="blue", command=floordiv)
    floordivbtn.place(x=130, y=220)

    logbtn = ctk.CTkButton(top, text="log", width=40, fg_color="green", hover_color="blue", command=log)
    logbtn.place(x=30, y=260)

    divbtn = ctk.CTkButton(top, text="/", width=40, fg_color="green", hover_color="blue", command=div)
    divbtn.place(x=80, y=260)

    factbtn = ctk.CTkButton(top, text="fact", width=40, fg_color="green", hover_color="blue", command=fact)
    factbtn.place(x=130, y=260)

    # Entry fields
    e1 = ctk.CTkEntry(top,corner_radius=10)
    e1.place(x=30, y=68)

    e2 = ctk.CTkEntry(top,corner_radius=10)
    e2.place(x=30, y=117)
   
    def on_enter_e1(event):
        e1.configure(border_color="green")

    def on_leave_e1(event):
        e1.configure(border_color="gray")

    def on_enter_e2(event):
        e2.configure(border_color="green")

    def on_leave_e2(event):
        e2.configure(border_color="gray")

# Bind
    e1.bind("<Enter>", on_enter_e1)
    e1.bind("<Leave>", on_leave_e1)

    e2.bind("<Enter>", on_enter_e2)
    e2.bind("<Leave>", on_leave_e2)
    # Result label
    label_result = ctk.CTkLabel(top, text="Result:")
    label_result.place(x=30, y=350)

    top.mainloop()
