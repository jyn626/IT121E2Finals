filename = "notes.txt"

try:
    note1 = input("Enter a note: ")
    with open(filename, "w") as file:
        file.write(note1 + "\n")
    print("Note Saved successfully! :)\n")

except Exception as e:
    print("File handling Error:", e)


try:
    print("File Contents: ")
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

try:
    note2 = input("\nEnter another note: ")
    with open(filename, "a") as file:
        file.write(note2 + "\n")

    print("\nNote Updated!: ")
    with open(filename, "r") as file:
        print(file.read())

except Exception as e:
    print("Error appending file:", e)
