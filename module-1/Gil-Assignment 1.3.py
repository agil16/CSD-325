#Arely Gil
#October 23, 2024
#Module 1.3

#Ask the user how many bottles of beer are on the wall.
#Pass that input to a function that manages the countdown.
#The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
#Once the count is down to 1, change lyrics to show "1 bottle of beer..."
#At the end of the countdown, get back to the main program and remind the user to buy more beer.

def countdown_beer_bottles(bottles):
    for i in range(bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.\n")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.\n")

def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles <= 0:
            print("Please enter a positive number.")
            return
        countdown_beer_bottles(bottles)
        print("NEED to buy MORE beer!")
    except ValueError:
        print("ERROR:Please enter a valid number.")

main()
