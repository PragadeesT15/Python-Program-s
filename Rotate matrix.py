# wap to rotate a given matrix to 90 degerry to right site and display the output and make should no.of row and col should be same?
row = int(input("Enter the number of row for matrix: "))
col = int(input("Enter the number of columns for matrix: "))
matrix =[[int(input("Enter The Number: ")) for i in range(col)]for j in range(row)]
print("Original Matrix")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
print("Rotate Matrix")
# 90-degree clockwise rotation: transpose then reverse each row
for i in range(col):
    for j in range(row):
        print(matrix[row-1-j][i], end=" ")
    print()