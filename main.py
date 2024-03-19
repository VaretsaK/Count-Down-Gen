def count_down(number: int):
    """
    A generator function that counts down from the given number to 0.

    Parameters:
    number (int): The starting number to count down from.

    Yields:
    int: The next number in the countdown.
    """
    for n in range(number, -1, -1):
        yield n


def main() -> None:
    for i in count_down(9):
        print(i)


if __name__ == "__main__":
    main()
