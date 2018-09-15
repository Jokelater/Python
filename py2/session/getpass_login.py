import getpass
username = raw_input("name:")
password = getpass.getpass("password:")
if username == 'tom' and password == '123':
    print("login")
else:
    print("error,try again!")