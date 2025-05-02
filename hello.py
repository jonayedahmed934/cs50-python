def numchecker():
    while True:

        try:
            return int(input("what's the number?: "))
        except ValueError:
            pass

x = numchecker()
print(x)
print("doen")

