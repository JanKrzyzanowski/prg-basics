trans_in_euro =[
    15.90,
    38.47,
    4.07,
    132.70,
    9.15,
]

transactions_in_pln = list(map(lambda x:x*4.5, trans_in_euro))

print(transactions_in_pln)
