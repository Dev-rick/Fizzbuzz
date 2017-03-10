
print "Welcome to fizzbuzz!\nEnter a number between 1 and 100 and guess why fizz or buzz or fizzbuzz appears"

while True:
    try:
        choice = int(raw_input("Enter her your number:\n>> "))
        print "Your number is", choice
        print "\n"

        if choice < 1 or choice > 100:
            print "Sorry, it has to be a number between 1 and 100"
            continue
        else:
            for i in range(choice):
                t = i + 1
                if t % 3 == 0 and t % 5 == 0:
                    print "fizzbuzz"
                elif t % 3 == 0:
                    print "fizz"
                elif t % 5 == 0:
                    print "buzz"
                else:
                    print t
            break
    except ValueError:
        print "OOPS that was no number, try again!"
        continue







