'''Calculate income tax to be paid by the emp[loyee by taking his annual income,hra,other daductions as input.
The rate of tax is:
    below 3 lakhs - no tax
    between 3 lakhs to 6 lakhs - 10% intrest
    between 6 lakhs to 10 lakhs - 15% intrest
    above 10 lakhs - 20% intrest'''

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
