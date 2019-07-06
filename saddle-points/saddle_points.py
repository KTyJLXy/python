def saddle_points(matrix):
    if matrix == []:
        return [{}]
    #Vars
    points = []
    position = {}
    columns = {}
    rows = {}
    lenrow = len(matrix[0])
    
    for row in matrix:
        if len(row) != lenrow:
            raise ValueError ("Invalid matrix")
    
    for row in matrix:
        for element in row:
            try:
                columns[row.index(element)]= columns[row.index(element)] + [element]
            except:
                columns[row.index(element)]= [element]
                
    for count, row in enumerate(matrix):
        rows[count]= row
            
    for count_row, row in enumerate(rows):
        for count_column, element in enumerate(rows[row]):
            if element == max(rows[row]):
                if element == min(columns[count_column]):
                    position["row"]= count_row + 1
                    position["column"]= count_column + 1
                    points.append(position)
                    
    if points == []:
        return [{}]
    return points
                



