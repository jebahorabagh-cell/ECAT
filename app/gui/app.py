import tkinter as tk
from app.services.startup import initialize

APP_NAME="ECAT - Excel Comparison & Audit Tool"
VERSION="Build 1.0.0"

def center(win,w=1100,h=700):
    sw=win.winfo_screenwidth(); sh=win.winfo_screenheight()
    x=(sw-w)//2; y=(sh-h)//2
    win.geometry(f"{w}x{h}+{x}+{y}")

def run_app():
    initialize()
    r=tk.Tk()
    r.title(f"{APP_NAME} ({VERSION})")
    center(r)
    r.minsize(900,600)
    tk.Label(r,text=APP_NAME,font=("Segoe UI",18,"bold")).pack(pady=20)
    tk.Label(r,text="Foundation Build Ready").pack()
    status=tk.Label(r,text="Status: Ready",anchor="w")
    status.pack(side="bottom",fill="x")
    r.mainloop()
