# Write a menu driven program to implement the following methods on List.
# (1) Create (2) Update particular element of list (3) Append to the list
# (4) Delete whole list (5) Delete particular element (6) Sort the list (7) Find length

my_list = [9, 2, 1, 4, 7, 6]
my_list1 = [8, 9, 10]


def list_display():
    print("Display List", my_list)


def list_update():
    print(my_list[2])
    my_list[2] = 300
    print("Updated List", my_list)


def list_append():
    my_list.append(7)
    print("Origial List", my_list)
    my_list.append(my_list1)
    print("After Appending List", my_list)


def list_clear():
    my_list1.clear()
    print("After Deleting List", my_list1)


def list_remove():
    my_list.remove(4)
    print("After removing List", my_list)


def list_sort():
    my_list.sort()
    print("After sorting List", my_list)


def list_len():
    x = len(my_list)
    print("List length", x)


# Menu Driven Heading

print("WELCOME TO LIST FUNCTIONS\n")

# using the while loop to print menu list

while True:
    print("MENU")
    print("1. LIST Display")
    print("2. Update particular element of list")
    print("3. Append to the list")
    print("4. Delete whole list")
    print("5. Delete particular element")
    print("6. Sort the list")
    print("7. Find length")
    print("8. Exit")

    users_choice = int(input("\nEnter your Choice: "))
    # based on the users choice the relevant method is called

    if users_choice == 1:
        list_display()
    elif users_choice == 2:
        list_update()
    elif users_choice == 3:
        list_append()
    elif users_choice == 4:
        list_clear()
    elif users_choice == 5:
        list_remove()
    elif users_choice == 6:
        list_sort()
    elif users_choice == 7:
        list_len()
    elif users_choice == 8:
        break
    else:
        print("Please enter a valid Input from the list")
