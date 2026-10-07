A = input("Enter status of Room A (Dirty/Clean): ")
B = input("Enter status of Room B (Dirty/Clean): ")

rooms = {
    "A": A,
    "B": B
}

position = input("Enter vacuum position (A/B): ").upper()

while "Dirty" in rooms.values():

    print("\nVacuum is in Room", position)

    if rooms[position] == "Dirty":
        print("Room", position, "is Dirty")
        print("Action: SUCK")
        rooms[position] = "Clean"

    else:
        print("Room", position, "is Clean")

        if position == "A":
            print("Action: MOVE RIGHT")
            position = "B"
        else:
            print("Action: MOVE LEFT")
            position = "A"

print("\nAll rooms are Clean!")
print("Final state:", rooms)
