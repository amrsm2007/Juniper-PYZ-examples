#!/usr/bin/python3
from tkinter import * # (1)
from jnpr.junos import Device
from jnpr.junos.exception import *
from pprint import pformat
USER = "root" # (2)
PASSWD = "root123"
DEVICE_IP = "127.0.0.1"
PORT="11"
def output(st): # (3)
    text.insert(END, chars=st)
    text.see(END)
def read_and_display(message, function): # (4)
    output(message)
    try:
        with Device(host=entry_dev.get(), user=entry_user.get(),
                password=entry_pw.get(),port=entry_port.get() ,mode="telnet") as dev:
         res = function(dev)
    except ConnectRefusedError:
        print("\nError: Connection refused!\n")
    except ConnectTimeoutError:
        output("\nConnection timeout error!\n")
    except ConnectUnknownHostError:
        output("\nError: Connection attempt to unknown host.\n")
    except ConnectionError:
        output("\nConnection error!\n")
    except ConnectAuthError:
        output("\nConnection authentication error!\n")
    else:
        output(res)
def print_facts(): # (5)
    read_and_display("\nDevice facts:\n", lambda dev: pformat(dev.facts))
def show_bgp(): # (6)
    read_and_display("\nBGP summary information:",
lambda dev: dev.rpc.get_isis_adjacency_information({"format": "text"}).text)
def show_intf(): # (7)
    read_and_display("\nInterface information:",
lambda dev: dev.rpc.get_interface_information({"format": "text"}, terse=True).text)
def main(): # (8)
        global entry_dev, entry_user, entry_pw,entry_port, text
        root = Tk() # (9)
        Frame(root, height=10).grid(row=0) # (10)
        Label(root, text="Device address:").grid(row=1, column=0) # (11)
        entry_dev = Entry(root) # (12)
        entry_dev.grid(row=1, column=1)
        entry_dev.insert(END, DEVICE_IP)
        Label(root, text="Login:").grid(row=2, column=0) # (13)
        entry_user = Entry(root)
        entry_user.grid(row=2, column=1)
        entry_user.insert(END, USER)
        Label(root, text="Password:").grid(row=3, column=0) # (14)
        entry_pw = Entry(root, show="*")
        entry_pw.grid(row=3, column=1)
        entry_pw.insert(END, PASSWD)
        Label(root, text="PORT:").grid(row=4, column=0)
        entry_port = Entry(root) # (12)
        entry_port.grid(row=4, column=1)
        entry_port.insert(END, PORT)
        Frame(root, height=10).grid(row=5) # (15)
        Button(root, text="Read facts!", command=print_facts).grid(row=6, column=0)
        Button(root, text="Show interfaces!", command=show_intf).grid(row=6, column=1)
        Button(root, text="Show BGP!", command=show_bgp).grid(row=6, column=2)
        Frame(root, height=10).grid(row=7)
        frame = Frame(root, width=800, height=700) # (16)
        frame.grid(row=8, column=0, columnspan=4)
        frame.grid_propagate(False)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        text = Text(frame, borderwidth=3)
        text.config(font=("courier", 11), wrap='none')
        text.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        scrollbarY = Scrollbar(frame, command=text.yview) # (17)
        scrollbarY.grid(row=0, column=1, sticky='nsew')
        text['yscrollcommand'] = scrollbarY.set
        scrollbarX = Scrollbar(frame, orient=HORIZONTAL, command=text.xview)
        scrollbarX.grid(row=1, column=0, sticky='nsew')
        text['xscrollcommand'] = scrollbarX.set
        root.mainloop() # (18)
if __name__ == "__main__": # (12)

    main()



