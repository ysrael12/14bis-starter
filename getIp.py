import socket
import webbrowser

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def browse_server():
    webbrowser.open('http://{}/Biblivre5/'.format(get_ip_address()))
