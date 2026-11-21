def printFib(n):

    # Handle invalid input
    if n < 1:
        print("Invalid Number of terms")
        return

    # Initialize first two Fibonacci numbers
    prev2 = 0
    prev1 = 1

    # Print first Fibonacci number
    print(prev2, end=" ")

    # If n is 1, stop here
    if n == 1:
        return

    # Print second Fibonacci number
    print(prev1, end=" ")

    # Generate Fibonacci numbers from 3rd term
    for i in range(3, n + 1):
        curr = prev1 + prev2

        print(curr, end=" ")

        # Update previous numbers
        prev2 = prev1
        prev1 = curr



