while True:
    while True:
        q= input("Do you want to add new value?(y/n)")
        if q in ('y','n'):
            break
        print("invalid input")
    print("in this 1st loop")
    if q == "y":
        continue
    else:
        break