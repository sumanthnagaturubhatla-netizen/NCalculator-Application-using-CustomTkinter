import customtkinter as ctk
def weightcon():
   top=ctk.CTk()
   top.geometry("500x650")
   top.title("weight converter")
   la=ctk.CTkLabel(top,text="Weight Converter",font=("Arial",25))
   la.place(x=30,y=45)
   la1=ctk.CTkLabel(top,text="Enter the weight value",font=("Arial",25))
   la1.place(x=30,y=75)
   e1=ctk.CTkEntry(top,placeholder_text="Enter the value in KILOGRAM",border_width=2,border_color="grey",corner_radius=10,width=300)
   e1.place(x=30,y=109)
   e2=ctk.CTkEntry(top,placeholder_text="ENTER GRAM, MG, POUND, OUNCE, TON VALUES",border_width=2,border_color="grey",corner_radius=10,width=300)
   e2.place(x=30,y=150)
   
   def on_enter(event):
      e1.configure(border_color="green")
   
   def on_leave(event):
      e1.configure(border_color="gray")
   
   e1.bind("<Enter>",on_enter)
   e1.bind("<Leave>",on_leave)
   
   def on_enter(event):
      e2.configure(border_color="green")
   
   def on_leave(event):
      e2.configure(border_color="gray")
   
   e2.bind("<Enter>",on_enter)
   e2.bind("<Leave>",on_leave)
   
   def kgtog():
      kg=int(e1.get())
      g=kg*1000
      e2.delete(0,"end")
      e2.insert(0,str(g))
   
   def kgtomg():
      kg=int(e1.get())
      mg=kg*1000000
      e2.delete(0,"end")
      e2.insert(0,str(mg))
   
   def kgtolb():
      kg=int(e1.get())
      lb=kg*2.20462
      e2.delete(0,"end")
      e2.insert(0,str(lb))
   
   def kgtooz():
      kg=int(e1.get())
      oz=kg*35.274
      e2.delete(0,"end")
      e2.insert(0,str(oz))
   
   def kgtoton():
      kg=int(e1.get())
      ton=kg/1000
      e2.delete(0,"end")
      e2.insert(0,str(ton))
   
   def gtokg():
      g=int(e2.get())
      kg=g/1000
      e1.delete(0,"end")
      e1.insert(0,str(kg))
      
   def mgtokg():
      mg=int(e2.get())
      kg=mg/1000000
      e1.delete(0,"end")
      e1.insert(0,str(kg))
   
   def lbtokg():
       lb=int(e2.get())
       kg=lb/2.20462
       e1.delete(0,"end")
       e1.insert(0,str(kg))
   
   def oztokg():
      oz=int(e2.get())
      kg=oz/35.274
      e1.delete(0,"end")
      e1.insert(0,str(kg))
   
   def tontokg():
      ton=int(e2.get())
      kg=ton*1000
      e1.delete(0,"end")
      e1.insert(0,str(kg))
   
   btn1=ctk.CTkButton(top,text="kilograms into grams",fg_color="green",hover_color="blue",command=kgtog)
   btn1.place(x=30,y=200)
   btn2=ctk.CTkButton(top,text="kilograms into milligrams",fg_color="green",hover_color="blue",command=kgtomg)
   btn2.place(x=30,y=240)
   btn3=ctk.CTkButton(top,text="kilograms into pounds",fg_color="green",hover_color="blue",command=kgtolb)
   btn3.place(x=30,y=280)
   btn4=ctk.CTkButton(top,text="kilograms into ounces",fg_color="green",hover_color="blue",command=kgtooz)
   btn4.place(x=30,y=320)
   btn5=ctk.CTkButton(top,text="kilograms into ton",fg_color="green",hover_color="blue",command=kgtoton)
   btn5.place(x=30,y=360)
   btn6=ctk.CTkButton(top,text="grams into kilograms",fg_color="green",hover_color="blue",command=gtokg)
   btn6.place(x=30,y=400)
   btn7=ctk.CTkButton(top,text="milligrams into kilograms",fg_color="green",hover_color="blue",command=mgtokg)
   btn7.place(x=30,y=440)
   btn8=ctk.CTkButton(top,text="pounds into kilograms",fg_color="green",hover_color="blue",command=lbtokg)
   btn8.place(x=30,y=480)
   btn9=ctk.CTkButton(top,text="ounces into kilograms",fg_color="green",hover_color="blue",command=oztokg)
   btn9.place(x=30,y=520)
   btn10=ctk.CTkButton(top,text="ton into kilograms",fg_color="green",hover_color="blue",command=tontokg)
   btn10.place(x=30,y=560)
   top.mainloop()