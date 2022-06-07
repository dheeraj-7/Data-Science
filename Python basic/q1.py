ai=float(input('Enter annual income: '))
hra=float(input('Enter HRA: '))
ded=float(input('Enter other deductions: '))
if ded>80000:
    ded=80000
tax_amt=ai-hra-ded
if tax_amt<=300000:
    print('No tax')
elif 300000<tax_amt<=600000:
    tax_amt=tax_amt-300000
    print(0.1*tax_amt)
elif 600000<tax_amt<=1000000:
    tax_amt=tax_amt-300000
    print(0.15*tax_amt)
else:
    tax_amt=tax_amt-300000
    print(0.2*tax_amt)    