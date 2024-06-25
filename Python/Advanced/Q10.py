def customers_without_computer(N, S):
    customer_status = {}
    occomp = set()
    count = 0

    for char in S:
        if char not in customer_status:
            if len(occomp) < N:
                occomp.add(char)
                customer_status[char] = 'using'
            else:
                count += 1
                customer_status[char] = 'walked_away'
        else:
            if customer_status[char] == 'using':
                occomp.remove(char)
    return count


N1 = 3
S1 = "GACCBDDBAGEE"
print(customers_without_computer(N1, S1))

N2 = 1
S2 = "ABCBAC"
print(customers_without_computer(N2, S2))
