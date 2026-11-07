#Name: Mudassir Munir 
#PSEB ID: PSEB-2026-010784
#Date: 07-11-2026    

#Part 4 - Collections in Python

#Warm Up Exercise:

print("===============Shopping List================")
items=["Milk", "Bread", "Eggs"]

items.append("Butter")
items.remove("Bread")
items.sort()

for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")


# Build:
#Phone Book

print("===============Phone Book================")
phone_book={
    "Ali": "0300-1234567",
    "Shahbaz": "0301-7654321",
    "Shah Fahad": "0302-9876543",
    "Huzaifa": "0303-4567890",
    "Danyal": "0304-2345678"

}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name=input("Enter contact name: ")
        number=input("Enter contact number: ")

        phone_book[name]=number
        print(f"Contact {name} added successfully.")

    elif choice == "2":
        name=input("Enter contact name to search: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print(f"Contact {name} not found.")

    elif choice == "3":
        name= input("Enter contact name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    elif choice == "4":
        if len(phone_book) == 0:
            print("No contacts found.")
        else:
            print("All Contacts:")
            for name, number in phone_book.items():
                print(f"{name}: {number}")

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")


# Challenge:
#create 
result_sheet = {
    "Ali": [85, 90, 78],
    "Shahbaz": [92, 88, 95],
    "Shah Fahad": [75, 80, 82],
    "Huzaifa": [88, 91, 89],
    "Danyal": [95, 94, 96]
}

highest_total = -1
topper = ""

below_40=set()

for student, marks in result_sheet.items():
    total=sum(marks)
    average=total/len(marks)

    print(f"\nStudent: {student}")