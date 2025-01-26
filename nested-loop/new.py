for i in range(8):            # Outer loop for rows
    for j in range(8):        # Inner loop for columns
        if (i + j) % 2 == 0:  # Check if the sum of row and column indexes is even
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()                   # Move to the next line
