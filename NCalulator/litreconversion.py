import customtkinter as ctk

def litrecon():
   top = ctk.CTk()
   top.geometry("300x500")
   top.title("Litre Converter")

   la = ctk.CTkLabel(top, text="Litre Converter", font=("Arial",25))
   la.place(x=30, y=40)

   e1 = ctk.CTkEntry(top, placeholder_text="Enter value in Litres",
                     border_width=2, border_color="grey",
                     corner_radius=10, width=250)
   e1.place(x=30, y=90)

   e2 = ctk.CTkEntry(top, placeholder_text="Result",
                     border_width=2, border_color="grey",
                     corner_radius=10, width=250)
   e2.place(x=30, y=140)

   # 🔥 Hover effects
   def on_enter_e1(event):
      e1.configure(border_color="green")

   def on_leave_e1(event):
      e1.configure(border_color="gray")

   def on_enter_e2(event):
      e2.configure(border_color="green")

   def on_leave_e2(event):
      e2.configure(border_color="gray")

   e1.bind("<Enter>", on_enter_e1)
   e1.bind("<Leave>", on_leave_e1)

   e2.bind("<Enter>", on_enter_e2)
   e2.bind("<Leave>", on_leave_e2)

   # ✅ Conversions

   # 1. L → mL
   def l_to_ml():
      l = float(e1.get())
      ml = l * 1000
      e2.delete(0, "end")
      e2.insert(0, str(ml))

   # 2. mL → L
   def ml_to_l():
      ml = float(e2.get())
      l = ml / 1000
      e1.delete(0, "end")
      e1.insert(0, str(l))

   # 3. L → kL
   def l_to_kl():
      l = float(e1.get())
      kl = l / 1000
      e2.delete(0, "end")
      e2.insert(0, str(kl))

   # 4. kL → L
   def kl_to_l():
      kl = float(e2.get())
      l = kl * 1000
      e1.delete(0, "end")
      e1.insert(0, str(l))

   # 5. L → m³
   def l_to_m3():
      l = float(e1.get())
      m3 = l / 1000
      e2.delete(0, "end")
      e2.insert(0, str(m3))

   # 🔘 Buttons
   btn1 = ctk.CTkButton(top, text="Litre → Millilitre",
                        fg_color="green", hover_color="blue",
                        command=l_to_ml)
   btn1.place(x=30, y=200)

   btn2 = ctk.CTkButton(top, text="Millilitre → Litre",
                        fg_color="green", hover_color="blue",
                        command=ml_to_l)
   btn2.place(x=30, y=240)

   btn3 = ctk.CTkButton(top, text="Litre → Kilolitre",
                        fg_color="green", hover_color="blue",
                        command=l_to_kl)
   btn3.place(x=30, y=280)

   btn4 = ctk.CTkButton(top, text="Kilolitre → Litre",
                        fg_color="green", hover_color="blue",
                        command=kl_to_l)
   btn4.place(x=30, y=320)

   btn5 = ctk.CTkButton(top, text="Litre → Cubic Meter",
                        fg_color="green", hover_color="blue",
                        command=l_to_m3)
   btn5.place(x=30, y=360)

   top.mainloop()