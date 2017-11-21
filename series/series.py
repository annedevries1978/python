def slices(series, length):
    start = 0
    end = length
    result_list = []
    if length == 0 or length > len(series):
        raise ValueError
    else:
        for x, y in enumerate(series):
            if length == len(series[start:end]):
                # print(x, x+1)
                result = series[start:end]
                end += 1
                start += 1
                z =[int(a) for a in list(result)]
                result_list.append(z)

        return result_list


#print(slices('2346780', 10))
print(slices("01234", 0))