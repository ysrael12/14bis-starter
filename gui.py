from getIp import browse_server, get_ip_address
from makeBackup import fazerbackup
import tkinter as tk
import qrcode
from PIL import Image, ImageTk


def makebackup():
    fazerbackup()

def start_btn_click():
    browse_server()


def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img


def create_gui(window):
    frame = tk.Frame(window)
    frame.pack(expand=True, fill='both')

    mkbackup = tk.Button(frame, padx=20, pady=10, text="Fazer Backup", command=makebackup,  bg='blue', fg='white')
    start_btn = tk.Button(frame, padx=20, pady=10, text="Abrir Biblivre V", command=start_btn_click, bg='green', fg='white')

    mkbackup.pack(pady=20)  # Adjusted padding for "Fazer Backup" button
    start_btn.pack(pady=20)  # Adjusted padding for "Ver link" button

    link = 'http://{}/Biblivre5/'.format(get_ip_address())  # Replace with your link
    qr_img = generate_qr_code(link)

    # Convert the QR code image to a format that Tkinter can display
    qr_img_tk = ImageTk.PhotoImage(qr_img)

    # Create a label to display the QR code
    qr_label = tk.Label(image=qr_img_tk)
    qr_label.image = qr_img_tk
    qr_label.pack(pady=1)

def create_window():
    window = tk.Tk()
    window.geometry("500x500")  # Adjusted window size for better visibility
    window.title("14 Bis starter")
    create_gui(window)
    
    window.mainloop()

create_window()
