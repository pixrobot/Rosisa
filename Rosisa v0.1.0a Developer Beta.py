import socket

print("The default password is password")
print("Insert password: ")
password = input()
if 'password' in password:
    print("Password Correct!")
    print("These are the things you can currently do with Rosisa:")
    print("To scan an IP Address for open ports just type: Scan an IP Address for open ports without showing closed ports or Scan an IP Address for open ports showing closed ports")
    print("To open a document just type: Open a document")
    print("To see information about me just type: Info")
    print("To see how i have been made better just type: Changelog")
    print("To say goodbye just type: Exit")
    print("To use the calculator just type: Use the calculator")
    print("To read the calculator instructions just type: Read calculator instructions")
    print("To see where i learned this stuff just type: Credits (only contains material i used after 13.03.2023)")
    print("If it asks you What would you like to do today it problably didnt understand you")
    while True:
        what_to_do_today = input("What would you like to do today?")

        if 'Credits' in what_to_do_today:
            print("<==[CALCULATOR CREDITS]==>")
            print("https://www.programiz.com/python-programming/examples/calculator - Base code")
            print("https://bing.com/ AI Chat - Troubleshooting (yes i know bing, its actually good now)")

        if 'Read calculator instructions' in what_to_do_today:
            print(" <=====[CALCULATOR INSTUCTIONS]=====>")
            print("The following question: [Enter first number to use in operation] modifies the following value in storage (The letter M is the modified value) MM [operation] xx")
            print("The following question: [Enter second number to use in operation] modifies the following value in storage (The letter M is the modified value) xx [operation] MM")
            print("I hope you understand this lmao")

        if 'Open a document' in what_to_do_today:
            print("I have found 2 documents.")
            print("Document 1 - 09.02.2023 17:04")
            print("Document 2 - 09.02.2023 17:05")
            document_load = input("Which document would you like me to open?")
            if 'Document 1' in document_load:
                print("Test")
            else:
                pass
            if 'Document 2' in document_load:
                print("Test 2")
        else:
            pass
        if 'Exit' in what_to_do_today:
            print("Thanks for using Rosisa!")
            print("Goodbye!")
            break
        if 'How to fix Sorry, i couldnt understand you.?' in what_to_do_today:
            print("This program does not use AI to understand what you are saying. It is impossible to fix it. Well, not really. If you have knowledge on python programming you can change a few arguments in my program so i can understand you.")
            print("Oh and ignore the Sorry, i couldnt understand you up there. Its a bug i cant fix.")
        else:
            pass
        if 'Info' in what_to_do_today:
            print("Rosisa Developer Beta")
            print("Version v0.1.0a Public Beta Preview")
            print("13.03.2023")
            print("Made with love by Roland")
        else:
            pass
        if 'Changelog' in what_to_do_today:
            print("Version 0.1.0a - 13.03.2023")
            print("Finally.. a long awaited update..")
            print("Added calculator")
            print("Added loop code function (so the exit command is useful now)")
            print("Made some stuff more like beautiful")
            print("Added credits")
            print("Thats it lmao")
            print("Expect more tommorow")
            print("Version 0.0.2 - 10.02.2023")
            print("Rosisa Developer Beta Released to public")
            print("Version 0.0.2b - 10.02.2023")
            print("Added option to show closed ports or only show open ports on the portscanner")
            print("Updated port open text")
            print("Version 0.0.2a - 10.02.2023")
            print("IP Address portscanner added")
            print("Version 0.0.1 - 09.02.2023")
            print("Rosisa Developer Beta Released to public")
            print("Version 0.0.1e - 09.02.2023")
            print("Changelog added")
            print("Version 0.0.1d - 09.02.2023")
            print("Sorry, i couldnt understand you removed to fix bug")
            print("Version 0.0.1c - 09.02.2023")
            print("Info added")
            print("Version 0.0.1b - 09.02.2023")
            print("Exit added")
            print("Sorry, i couldnt understand you added")
            print("Version 0.0.1a - 09.02.2023")
            print("Open a document added")
            print("Base program ready")
        if 'Scan an IP Address for open ports showing closed ports' in what_to_do_today:
            print("Note: this may take a really long time")
            def scan(target, ports):
                print('\n' + ' Starting Scan For ' + str(target))
                for port in range(1, ports):
                    scan_port(target, port)


            def scan_port(ipaddress, port):
                try:
                    sock = socket.socket()
                    sock.connect((ipaddress, port))
                    print("____[+]____ Port " + str(port) + " Open! :)")
                    sock.close()
                except:
                    print("<---[-]---> Port " + str(port) + " Closed :(")


            targets = input("[*] What IP Address do you want me to scan, if you want to scan multiple, just split them with , without spaces!: ")
            ports = int(input("[*] Enter How Many Ports You Want To Scan for example, if you type 100, i will scan ports 1-100!: "))
            if ',' in targets:
                print("[*] Scanning Multiple IP Addresses!")
                for ip_addr in targets.split(','):
                    scan(ip_addr.strip(' '), ports)
            else:
                scan(targets, ports)
        if 'Scan an IP Address for open ports without showing closed ports' in what_to_do_today:
            print("Note: this may take a really long time")
            def scan(target, ports):
                print('\n' + ' Starting Scan For ' + str(target))
                for port in range(1, ports):
                    scan_port(target, port)


            def scan_port(ipaddress, port):
                try:
                    sock = socket.socket()
                    sock.connect((ipaddress, port))
                    print("[+] Port Opened " + str(port) + "!")
                    sock.close()
                except:
                    pass


            targets = input("[*] What IP Address do you want me to scan, if you want to scan multiple, just split them with , without spaces!: ")
            ports = int(input("[*] Enter How Many Ports You Want To Scan for example, if you type 100, i will scan ports 1-100!: "))
            if ',' in targets:
                print("[*] Scanning Multiple IP Addresses!")
                for ip_addr in targets.split(','):
                    scan(ip_addr.strip(' '), ports)
            else:
                scan(targets, ports)
        if 'Use the calculator' in  what_to_do_today:
            print("Welcome to the calculator!")
            print("These are the types of operations i can currently do: ")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            while True:
                calculator_operation_type = input("What type of operation would you like to do? 1/2/3/4: ")

                if calculator_operation_type in ('1', '2', '3', '4'):
                    try:
                        num1 = float(input("Enter first number to use in operation (Example in instructions): "))
                        num2 = float(input("Enter first second to use in operation (Example in instructions): "))
                    except ValueError:
                        print("Umm, number please! ")
                        continue

                    if calculator_operation_type == '1':
                        print(num1, "+", num2, "=", num1 + num2)

                    elif calculator_operation_type == '2':
                        print(num1, "-", num2, "=", num1 - num2)

                    elif calculator_operation_type == '3':
                        print(num1, "*", num2, "=", num1 * num2)

                    elif calculator_operation_type == '4':
                        print(num1, "/", num2, "=", num1 / num2)

                    print("I hope you are satisfied with my answer.")
                    calculator_repeat_code = input("Do you want to do another operation? (yes/no): ")
                    if calculator_repeat_code == "no":
                        break

else:
    print("Password Incorrect.")
