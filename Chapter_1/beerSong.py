word = "bottles"

for beer_number in range(99,0,-1):

    print(beer_number, word, "of beer on the wall.")
    print(beer_number, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")

    if beer_number == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_number - 1

        if new_num == 1:
            word = "bottle"

        print(new_num, word, "of beer on the wall.")

    print()
