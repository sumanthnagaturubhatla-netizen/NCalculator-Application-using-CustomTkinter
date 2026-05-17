import customtkinter as ctk
import math

def sphere():
    def volume():
        r = int(e1.get())
        vol = (4/3) * math.pi * r**3
        label_result.configure(text=f"Result: {vol}")

    def surface():
        r = int(e1.get())
        sa = 4 * math.pi * r**2
        label_result.configure(text=f"Result: {sa}")

    top = ctk.CTk()
    top.geometry("500x450")
    top.configure(bg_color="lightblue")
    top.title("Sphere Calculator")

    la = ctk.CTkLabel(top, text="Enter Radius:", font=("Arial", 14))
    la.place(x=30, y=40)

    e1 = ctk.CTkEntry(top, width=200, height=35)
    e1.place(x=30, y=70)

    btn1 = ctk.CTkButton(top, text="Calculate Volume",
                         fg_color="green", hover_color="blue",
                         command=volume)
    btn1.place(x=30, y=130)

    btn2 = ctk.CTkButton(top, text="Calculate Surface Area",
                         fg_color="green", hover_color="blue",
                         command=surface)
    btn2.place(x=30, y=180)

    # 🔥 Hover events (same style)

    def on_enter_e1(event):
        e1.configure(border_color="green")

    def on_leave_e1(event):
        e1.configure(border_color="gray")

    # Bind
    e1.bind("<Enter>", on_enter_e1)
    e1.bind("<Leave>", on_leave_e1)

    label_result = ctk.CTkLabel(top, text="Result", font=("Arial", 14))
    label_result.place(x=30, y=300)

    top.mainloop()