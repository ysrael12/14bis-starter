import socket
import webbrowser
from tkinter import *



def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def browse_server():
    webbrowser.open('http://{}/Biblivre5/'.format(get_ip_address()))

def start_btn_click():
    
    browse_server()

def create_window():
    window = Tk()
    window.geometry("500x500")
    window.title("14 Bis starter")
    start_btn = Button(window, padx=20, pady=10, text="Ver link", command=start_btn_click)
    start_btn.pack(padx=50, pady=200)
    window.mainloop()

create_window()