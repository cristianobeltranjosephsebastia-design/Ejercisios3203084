counter = 0
while counter < 10:
    if counter == 5:
        print("Skipping number 5")
        counter += 1
        continue
    print("Number:", counter)
    counter += 1

