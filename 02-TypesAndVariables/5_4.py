##Program that converts amount to vat%

vat = .23
amount = float(input('Input your amount: '))
vat_paid = amount*vat
print(f'The total amount of VAT paid was: {vat_paid}')
