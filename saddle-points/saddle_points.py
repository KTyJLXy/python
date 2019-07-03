def saddle_points(matrix):
    #Vars
    points = {}



class Matrix(object):
    #?
    def __init__(self, matrix_string):
        #Class variables
        self.matrix = []
        self.matrix_rows = {}
        self.matrix_columns = {}

        self.matrix = matrix_string.split('\n')
        i = 1
        j = 1
        for row in self.matrix:
            if i <= len(self.matrix): 
                self.matrix_rows[i] = self.get_row(i, self.matrix)
                i = i + 1
            if j <= len(self.matrix[0].split(' ')):
                self.matrix_columns[j] = self.get_column(j, self.matrix)
                j = j + 1

    def row(self, index):
        return self.matrix_rows[index]

    def column(self, index):
        return self.matrix_columns[index]

    def get_column(self, index, splitmatrix):
        column = []
        for row in splitmatrix:
            column = column + [int(row.split(' ')[index - 1])]
        return column
    
    def get_row(self, index, splitmatrix):
        row = []
        for value in splitmatrix[index - 1].split(' '):
            row = row + [int(value)]
        return row
    

