" MacSetup.py to automate the early setup procedure's for Macs"
#!/usr/local/bin/python
import subprocess

clients_list = []

class Client:
    def __init__(self, name, addigy):
        self.clientname = name
        self.addigy_download = addigy

    def print_obj(self):
        print(self.clientname)
        print(self.addigy_download)

def rename():
    name = raw_input("What is the computer name: ")
    subprocess.call(["sudo", "scutil", "--set", "LocalHostName", name])
    subprocess.call(["sudo", "scutil", "--set", "HostName", name])
    subprocess.call(["sudo", "scutil", "--set", "ComputerName", name])
    return

def add_client(client_list):
    clients = open("client.txt")
    while True:
        line = str(clients.readline()).strip()
        if not line: break
        client_name = line
        line = clients.readline()
        if not line: break
        addigy_download = line.split("&&")
        client_list.append(Client(client_name, addigy_download))
    clients.close()
    return

def install_addigy(clients):
    client_name = str(raw_input("Client name: "))+'\n'
    for x in range(len(clients_list)):
        print (x)
        name = str(clients_list[x].clientname)
    if (client_name == name):
        print ("installing addigy")
        subprocess.call(([clients[x].addigy_download[0]]))
        subprocess.call(([clients[x].addigy_download[1]]))
        subprocess.call(([clients[x].addigy_download[2]]))
        return

def all():
    client = raw_input("Client?: ")
    for x in range(len(clients_list)):
        if clients_list[x].clientname == client:
            rename()
            subprocess.call([clients_list[x].addigy_download])
            subprocess.call([clients_list[x].munki])
            return

def check_clients(client_list):
    for x in range(len(client_list)):
        print(client_list[x].clientname)
    return

def status(client_list):
    for x in range(len(client_list)):
        client_list[x].print_obj()
    return

def main_menu():
    while True:
        x = input("1 to rename, 2 to install addigy, 3 to run munki, 4 for all three, 5 to check client list: ")

        if x == "1":
            rename()
        elif x == "2":
            install_addigy(clients_list)
        elif x == "3":
            run_munki(clients_list)
        elif x == "4":
            all()
        elif x == "5":
            check_clients(clients_list)
        elif x == "18405087":
            status(clients_list)
        else:
            print("Not valid input\n")

def main():
    add_client(clients_list)
    main_menu()

if __name__ == "__main__":
    main()
