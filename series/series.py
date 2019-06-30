def slices(series, length):
    
    i = 0
    series_lst = []
    
    if length > len(series) or length <=0 or len(series) == 0:
        raise ValueError ('No series')
    
    for i in range(len(series) - length + 1):
        series_lst.append(series[i:i+length])
    
    return series_lst