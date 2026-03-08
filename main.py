ip = input("Enter IP: ")

parts = ip.split(".")

if len(parts) != 4:
    print("Invalid IP")
else:
    valid = True
    for p in parts:
        if not p.isdigit() or not 0 <= int(p) <= 255:
            valid = False

    if valid:
        print("Valid IP")
    else:
        print("Invalid IP")
