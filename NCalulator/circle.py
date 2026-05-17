import customtkinter as ctk
import math

def circle():
    def perimeter():
        r = int(e1.get())
        peri = 2 * math.pi * r
        label_result.configure(text=f"Result: {peri}")

    def area():
        r = int(e1.get())
        area_val = math.pi * r * r
        label_result.configure(text=f"Result: {area_val}")
    
    # Main window
    top = ctk.CTk()
    top.configure(bg_color="lightblue")
    top.geometry("500x450")
    top.title("Circle Calculator")

    Rad = ctk.CTkLabel(top, text="Enter the radius of a Circle:", font=("Arial", 14))
    Rad.place(x=30, y=50)

    # Entry field with neat adjustments
    e1 = ctk.CTkEntry(top, width=200, height=35, corner_radius=8, font=("Arial", 14))
    e1.place(x=30, y=75)

    # Buttons with consistent styling
    calper = ctk.CTkButton(top, text="Calculate Perimeter",
                           fg_color="green", hover_color="blue",
                           command=perimeter)
    calper.place(x=30, y=120)

    calarea = ctk.CTkButton(top, text="Calculate Area",
                            fg_color="green", hover_color="blue",
                            command=area)
    calarea.place(x=30, y=170)
    
    def on_enter_e1(event):
        e1.configure(border_color="green")

    def on_leave_e1(event):
        e1.configure(border_color="gray")
    
    e1.bind("<Enter>", on_enter_e1)
    e1.bind("<Leave>", on_leave_e1)

    # Result label
    label_result = ctk.CTkLabel(top, text="Result", font=("Arial", 14))
    label_result.place(x=30, y=350)

    top.mainloop()
