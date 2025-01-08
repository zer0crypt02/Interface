import netifaces
import tkinter as tk
from tkinter import ttk, messagebox

def get_interface_details():
    interfaces = netifaces.interfaces()
    interface_list = []

    for iface in interfaces:
        addresses = netifaces.ifaddresses(iface)
        ip_info = addresses.get(netifaces.AF_INET, [{}])[0]
        mac_info = addresses.get(netifaces.AF_LINK, [{}])[0]

        interface_details = {
            "Interface": iface,
            "IP Address": ip_info.get("addr", "N/A"),
            "Netmask": ip_info.get("netmask", "N/A"),
            "MAC Address": mac_info.get("addr", "N/A")
        }

        interface_list.append(interface_details)

    return interface_list

def display_interfaces_gui():
    def show_details():
        interface_list = get_interface_details()
        for iface in interface_list:
            tree.insert("", "end", values=(iface['Interface'], iface['IP Address'], iface['Netmask'], iface['MAC Address']))

        details_button.config(state=tk.DISABLED)

    # Pencere Oluştur
    root = tk.Tk()
    root.title("Ağ Arayüz Bilgileri")
    root.geometry("600x400")

    # Liste
    columns = ("Interface", "IP Address", "Netmask", "MAC Address")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("Interface", text="Arayüz")
    tree.heading("IP Address", text="IP Adresi")
    tree.heading("Netmask", text="Alt Ağ Maskesi")
    tree.heading("MAC Address", text="MAC Adresi")
    tree.column("Interface", width=100)
    tree.column("IP Address", width=150)
    tree.column("Netmask", width=150)
    tree.column("MAC Address", width=150)

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Buton
    details_button = ttk.Button(root, text="Ağ Bilgilerini Göster", command=show_details)
    details_button.pack(pady=20)

    # GUI Çalıştır
    root.mainloop()

if __name__ == "__main__":
    display_interfaces_gui()
