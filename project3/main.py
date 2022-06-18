from decimal import Decimal


def calculate_fee(written_checks: int) -> Decimal:
    """
    Calculates the bank fee for the number of checks written

    :param written_checks: how many checks were written
    :return: the fees for the number of checks written according to the schedule
    """
    fees = Decimal("10")
    if written_checks < 20:
        fees += written_checks * Decimal(".1")
    elif 20 <= written_checks < 40:
        fees += written_checks * Decimal(".08")
    elif 40 <= written_checks < 60:
        fees += written_checks * Decimal(".06")
    elif written_checks >= 60:
        fees += written_checks * Decimal(".04")

    return fees


if __name__ == "__main__":

    num_checks = -1
    while num_checks < 0:
        checks_input = input("What is the number of checks written this month? ")
        try:
            num_checks = int(checks_input)
            if num_checks < 0:
                print(">>> Invalid input: number of checks must be at least 0")
        except ValueError:
            print(">>> Invalid input: must be a number")

    fee = calculate_fee(num_checks)

    print(f"For writing {num_checks} checks, the bank fee is ${fee:.2f}")
