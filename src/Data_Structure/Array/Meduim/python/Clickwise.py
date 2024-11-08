def print_clickwise(matrix):
    if not matrix or not matrix[0]:
        return None
    
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    
    # Initialize boundaries
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    result = []
    
    while top <= bottom and left <= right:

        # Traverse the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        print(bottom)
        # Traverse the bottom row (if still within bounds)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        print(left,right)
        # Traverse the left column (if still within bounds)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    # Print result in the desired format
    print(result)

# Input matrix
matrix = [ 
    [1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12] ]

# Call the function to print in clickwise order
print_clickwise(matrix)
