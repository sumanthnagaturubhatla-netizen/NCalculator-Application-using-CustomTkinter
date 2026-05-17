import customtkinter as ctk
def tempcon():
   top=ctk.CTk()
   top.geometry("500x450")
   top.title("temperature converter")
   la=ctk.CTkLabel(top,text="Temperature Converter",font=("Arial",25))
   la.place(x=30,y=45)
   la1=ctk.CTkLabel(top,text="Enter the temperature value",font=("Arial",25))
   la1.place(x=30,y=75)
   e1=ctk.CTkEntry(top,placeholder_text="Enter the value in CELSIUS",border_width=2,border_color="grey",corner_radius=10,width=300)
   e1.place(x=30,y=109)
   e2=ctk.CTkEntry(top,placeholder_text="ENTER FAHRENHEIT, KELVIN VALUES",border_width=2,border_color="grey",corner_radius=10,width=300)
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
   
   def ctof():
      c=int(e1.get())
      f=(c*9/5)+32
      e2.delete(0,"end")
      e2.insert(0,str(f))
   
   def ctok():
      c=int(e1.get())
      k=c+273.15
      e2.delete(0,"end")
      e2.insert(0,str(k))
   
   def ftoc():
      f=int(e2.get())
      c=(f-32)*5/9
      e1.delete(0,"end")
      e1.insert(0,str(c))
      
   def ktoc():
      k=int(e2.get())
      c=k-273.15
      e1.delete(0,"end")
      e1.insert(0,str(c))
   
   btn1=ctk.CTkButton(top,text="celsius into fahrenheit",fg_color="green",hover_color="blue",command=ctof)
   btn1.place(x=30,y=200)
   btn2=ctk.CTkButton(top,text="celsius into kelvin",fg_color="green",hover_color="blue",command=ctok)
   btn2.place(x=30,y=240)
   btn3=ctk.CTkButton(top,text="fahrenheit into celsius",fg_color="green",hover_color="blue",command=ftoc)
   btn3.place(x=30,y=280)
   btn4=ctk.CTkButton(top,text="kelvin into celsius",fg_color="green",hover_color="blue",command=ktoc)
   btn4.place(x=30,y=320)
   
   top.mainloop()