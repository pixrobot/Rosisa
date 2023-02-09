print("The default password is password")
password = input("Insert password")
if 'password' in password:
    print("Password Correct!")
    print("These are the things you can currently do with Rosisa:")
    print("To open a document just type: Open a document")
    print("To see information about me just type: Info")
    print("To see how i have been made better just type: Changelog")
    print("To say goodbye just type: Exit")
    print("Note from creator: Yeahhhh its pretty boring what it can do right now as it doesnt use AI.")
    what_to_do_today = input("What would you like to do today?")
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
        pass
    if 'How to fix Sorry, i couldnt understand you.?' in what_to_do_today:
        print("This program does not use AI to understand what you are saying. It is impossible to fix it. Well, not really. If you have knowledge on python programming you can change a few arguments in my program so i can understand you.")
        print("Oh and ignore the Sorry, i couldnt understand you up there. Its a bug i cant fix.")
    else:
        pass
    if 'Info' in what_to_do_today:
        print("Rosisa Developer Beta")
        print("Version 0.0.1")
        print("09.02.2023")
        print("Made with love by Roland")
    else:
        pass
    if 'Changelog' in what_to_do_today:
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
else:
    print("Password Incorrect.")
