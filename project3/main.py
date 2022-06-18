
if __name__ == "__main__":

    num_checks = -1
    while num_checks < 0:
        checks_input = input("What is the number of checks written this month? ")
        try:
            num_checks = int(checks_input)
            if num_checks < 0:
                print(">>> Invalid input: must be 0 or greater")
        except ValueError:
            print(">>> Invalid input: must be a number")

    fee = 10
    if num_checks < 20:
        fee += num_checks * .1
    elif 20 >= num_checks < 40:
        fee += num_checks * .08
    elif 40 >= num_checks < 60:
        fee += num_checks * .06
    elif num_checks >= 60:
        fee += num_checks * .04

    print(f"For writing {num_checks} checks, the bank fee is ${fee:.2f}")
