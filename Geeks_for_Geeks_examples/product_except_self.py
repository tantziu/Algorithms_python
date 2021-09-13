def product_except_self(a):
    product = 1
    result =[]
    has_zero = False
    for i in a:
        if i != 0:
            product *= i
        if i == 0:
            if has_zero:
                return [0] * len(a)
            has_zero = True

    for j in a:
        if has_zero:
            if j == 0:
                result.append(product)
            else:
                result.append(0)
        else:
            result.append(int(product / j))

    return result

a1 = [10,3,5,6,2]
#output: [180, 600, 360, 300, 900]
a2 = [12, 1, 3, 1]
print(product_except_self(a2))
    
