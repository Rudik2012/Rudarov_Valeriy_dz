
a = [[31, 37, 51], [22, 23, 86]]
b = [[5, 3, 6], [4, 5, 14]]

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str,self.matrix))

    def __add__(self, other):
        c =[]
        for i in range(len(self.matrix)):
            c.append([])
            for j in range(len(self.matrix[0])):
                c[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str,c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(f"matrix_1\n{matrix_1}\n{'-' * 20}")
print(f"matrix_2\n{matrix_2}\n{'-' * 20}")
print(f"matrix_1 + matrix_2\n{matrix_1 + matrix_2}")