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
        for count_it, element in enumerate(row):
            try:
                columns[count_it]= columns[count_it] + [element]
            except:
                columns[count_it]= [element]
                
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
                



