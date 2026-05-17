import customtkinter as ctk

def cuboid():
    def volume():
        l = int(e1.get())
        b = int(e2.get())
        h = int(e3.get())
        vol = l * b * h
        label_result.configure(text=f"Result: {vol}")

    def surface():
        l = int(e1.get())
        b = int(e2.get())
        h = int(e3.get())
        sa = 2 * (l*b + b*h + h*l)
        label_result.configure(text=f"Result: {sa}")

    top = ctk.CTk()
    top.geometry("500x450")
    top.configure(bg_color="lightblue")
    top.title("Cuboid Calculator")

    lla = ctk.CTkLabel(top, text="Enter Length:", font=("Arial", 14))
    lla.place(x=30, y=40)

    bla = ctk.CTkLabel(top, text="Enter Breadth:", font=("Arial", 14))
    bla.place(x=30, y=100)

    hla = ctk.CTkLabel(top, text="Enter Height:", font=("Arial", 14))
    hla.place(x=30, y=160)

    e1 = ctk.CTkEntry(top, width=200, height=35)
    e1.place(x=30, y=70)

    e2 = ctk.CTkEntry(top, width=200, height=35)
    e2.place(x=30, y=130)

    e3 = ctk.CTkEntry(top, width=200, height=35)
    e3.place(x=30, y=190)

    btn1 = ctk.CTkButton(top, text="Calculate Volume",
                         fg_color="green", hover_color="blue",
                         command=volume)
    btn1.place(x=30, y=240)

    btn2 = ctk.CTkButton(top, text="Calculate Surface Area",
                         fg_color="green", hover_color="blue",
                         command=surface)
    btn2.place(x=30, y=290)

    # 🔥 Hover events (same style as your triangle/cube)

    def on_enter_e1(event):
        e1.configure(border_color="green")

    def on_leave_e1(event):
        e1.configure(border_color="gray")

    def on_enter_e2(event):
        e2.configure(border_color="green")

    def on_leave_e2(event):
        e2.configure(border_color="gray")

    def on_enter_e3(event):
        e3.configure(border_color="green")

    def on_leave_e3(event):
        e3.configure(border_color="gray")

    # Bind
    e1.bind("<Enter>", on_enter_e1)
    e1.bind("<Leave>", on_leave_e1)

    e2.bind("<Enter>", on_enter_e2)
    e2.bind("<Leave>", on_leave_e2)

    e3.bind("<Enter>", on_enter_e3)
    e3.bind("<Leave>", on_leave_e3)

    label_result = ctk.CTkLabel(top, text="Result", font=("Arial", 14))
    label_result.place(x=30, y=360)

    top.mainloop()