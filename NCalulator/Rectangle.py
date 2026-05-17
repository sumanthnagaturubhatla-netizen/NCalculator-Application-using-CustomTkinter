import customtkinter as ctk

def rectangle():
    def area():
        l = int(e1.get())
        b = int(e2.get())
        area_val = l * b
        label_result.configure(text=f"Result: {area_val}")

    def perimeter():
        l = int(e1.get())
        b = int(e2.get())
        peri_val = 2 * (l + b)
        label_result.configure(text=f"Result: {peri_val}")

    # Main window
    top = ctk.CTk()
    top.title("Rectangle Calculator")
    top.geometry("500x450")
    top.configure(bg_color="lightblue")

    length = ctk.CTkLabel(top, text="Enter the Length of a Rectangle:", font=("Arial", 14))
    length.place(x=30, y=40)

    breadth = ctk.CTkLabel(top, text="Enter the Breadth of a Rectangle:", font=("Arial", 14))
    breadth.place(x=30, y=95)

    # Entry fields with neat adjustments
    e1 = ctk.CTkEntry(top, width=200, height=35, corner_radius=8, font=("Arial", 14))
    e1.place(x=30, y=65)

    e2 = ctk.CTkEntry(top, width=200, height=35, corner_radius=8, font=("Arial", 14))
    e2.place(x=30, y=120)

    # Buttons with consistent styling
    areabtn = ctk.CTkButton(top, text="Calculate Area",
                            fg_color="green", hover_color="blue",
                            command=area)
    areabtn.place(x=30, y=160)

    peribtn = ctk.CTkButton(top, text="Calculate Perimeter",
                            fg_color="green", hover_color="blue",
                            command=perimeter)
    peribtn.place(x=30, y=200)
    
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
    label_result = ctk.CTkLabel(top, text="Result", font=("Arial", 14))
    label_result.place(x=30, y=350)

    top.mainloop()
