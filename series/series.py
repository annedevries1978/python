def slices(series, length):
    start = 0
    end = length
    for x, y in enumerate(series):
        while len(series[start:end]) == length:
            # print(x, x+1)
            result = series[start:end]
            end += 1
            start += 1
            print (result)


print(slices('2346780', 1))
