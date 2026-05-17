import customtkinter as ctk
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def on_click():
    speak("Button clicked")

top = ctk.CTk()
top.geometry("300x200")

btn = ctk.CTkButton(top, text="Click Me", command=on_click)
btn.pack(pady=50)

top.mainloop()