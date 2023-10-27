names = []

count = input("Podaj liczbe graczy: ")

print(count)
print(type(count))

count = int(count)

for i in range(0, count):
    name = input("Podaj imię i nazwisko: ")
    names.append(name)

counter = 0

for x in names:
    if counter == 1:
        x = x + " pizda"
    print(x)
    counter = counter + 1

print(names)
