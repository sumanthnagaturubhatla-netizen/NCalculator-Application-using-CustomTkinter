import customtkinter as ctk
import math

def cylinder():
    def volume():
        r = int(e1.get())
        h = int(e2.get())
        vol = math.pi * r**2 * h
        label_result.configure(text=f"Result: {vol}")

    def surface():
        r = int(e1.get())
        h = int(e2.get())
        sa = 2 * math.pi * r * (r + h)
        label_result.configure(text=f"Result: {sa}")

    top = ctk.CTk()
    top.geometry("500x450")
    top.configure(bg_color="lightblue")
    top.title("Cylinder Calculator")

    rla = ctk.CTkLabel(top, text="Enter Radius:", font=("Arial", 14))
    rla.place(x=30, y=40)

    hla = ctk.CTkLabel(top, text="Enter Height:", font=("Arial", 14))
    hla.place(x=30, y=100)

    e1 = ctk.CTkEntry(top, width=200, height=35)
    e1.place(x=30, y=70)

    e2 = ctk.CTkEntry(top, width=200, height=35)
    e2.place(x=30, y=130)

    btn1 = ctk.CTkButton(top, text="Calculate Volume",
                         fg_color="green", hover_color="blue",
                         command=volume)
    btn1.place(x=30, y=190)

    btn2 = ctk.CTkButton(top, text="Calculate Surface Area",
                         fg_color="green", hover_color="blue",
                         command=surface)
    btn2.place(x=30, y=240)

    # 🔥 Hover events (same style)

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

    label_result = ctk.CTkLabel(top, text="Result", font=("Arial", 14))
    label_result.place(x=30, y=320)

    top.mainloop()