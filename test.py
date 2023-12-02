import os
import requests
from ping3 import ping, verbose_ping
import tkinter as tk
import threading

def check_latency():
    paris_latency = int(ping("dynamodb.eu-west-3.amazonaws.com") * 1000)
    frankfurt_latency = int(ping("dynamodb.eu-central-1.amazonaws.com") * 1000)
    result_text.set(f"Valorant Paris Latency: {paris_latency}ms\nValorant Frankfurt Latency: {frankfurt_latency}ms ")
    
def start_check_latency():
    threading.Thread(target=check_latency).start()
    root.after(1000, start_check_latency)  # schedule the next check

root = tk.Tk()
root.title("Valorant Ping")

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack(padx=50, pady=50)

root.after(1000, start_check_latency) 

root.mainloop()