alpha = ' apple is a good product!  '


def split(alpha, cut):
    length = len(alpha)
    point = 0
    result = []

    for i in range(length):
        if alpha[i] == cut:
            result.append(alpha[point:i])
            point = i+1
    return result


print(split(alpha, " "))
