import customtkinter as ctk

def square():
    def perimeter():
        s = int(e1.get())
        peri = 4 * s
        label_result.configure(text=f"Result: {peri}")

    def area():
        s = int(e1.get())
        area_val = s * s
        label_result.configure(text=f"Result: {area_val}")

    # Main window
    top = ctk.CTk()
    top.title("Square Calculator")
    top.geometry("500x450")
    top.configure(bg_color="lightblue")

    # Label for side
    squrLb = ctk.CTkLabel(top, text="Enter the side of a square:", font=("Arial", 14))
    squrLb.place(x=30, y=40)

    # Entry field with neat adjustments
    e1 = ctk.CTkEntry(top, width=200, height=35, corner_radius=8, font=("Arial", 14))
    e1.place(x=30, y=70)

    # Buttons with consistent styling
    calperim = ctk.CTkButton(top, text="Calculate Perimeter",
                             fg_color="green", hover_color="blue",
                             command=perimeter)
    calperim.place(x=30, y=130)

    calarea = ctk.CTkButton(top, text="Calculate Area",
                            fg_color="green", hover_color="blue",
                            command=area)
    calarea.place(x=30, y=180)
    
    def on_enter_e1(event):
       e1.configure(border_color="green")

    def on_leave_e1(event):
       e1.configure(border_color="gray")

    # Correct binding
    e1.bind("<Enter>", on_enter_e1)   # ✅ enter → green
    e1.bind("<Leave>", on_leave_e1)   # ✅ leave → gray
    # Result label
    label_result = ctk.CTkLabel(top, text="Result:", font=("Arial", 14))
    label_result.place(x=30, y=350)

    top.mainloop()
