import customtkinter as ctk

def triangle():
    def area():
        b = int(e1.get())
        h = int(e2.get())
        area_val = 0.5 * b * h
        label_result.configure(text=f"Result: {area_val}")

    def perimeter():
        s = int(e1.get())
        peri_val = 3 * s
        label_result.configure(text=f"Result: {peri_val}")

    # Main window
    top = ctk.CTk()
    top.geometry("500x450")
    top.configure(bg_color="lightblue")
    top.title("Triangle Calculator")

    # Labels
    basela = ctk.CTkLabel(top, text="Enter the Base or side of a Triangle:", font=("Arial", 14))
    basela.place(x=30, y=40)

    heightla = ctk.CTkLabel(top, text="Enter the height of a Triangle:", font=("Arial", 14))
    heightla.place(x=30, y=100)

    # Entry fields with neat adjustments
    e1 = ctk.CTkEntry(top, width=200, height=35, corner_radius=8, font=("Arial", 14))
    e1.place(x=30, y=70)

    e2 = ctk.CTkEntry(top, width=200, height=35, corner_radius=8, font=("Arial", 14))
    e2.place(x=30, y=130)

    # Buttons with consistent styling
    calarea = ctk.CTkButton(top, text="Calculate Area",
                            fg_color="green", hover_color="blue",
                            command=area)
    calarea.place(x=30, y=180)

    calPer = ctk.CTkButton(top, text="Calculate Perimeter",
                           fg_color="green", hover_color="blue",
                           command=perimeter)
    calPer.place(x=30, y=230)
    
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
