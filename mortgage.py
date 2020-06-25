# Program name    : Functions.
# Program purpose : Modify the mortgage.py program function that will calculate mortgage payment.And also using keyword "import" to add in calculateMenu.py
# Created/revised : on 4/18/2020 jeff 
# This program calculates the mortgage payment
"""
Write the mortgage function to calculate mortgage payment.
(HINT:  Use simpleInterest.py as an example to write this function.

How to calculate mortgage payment:
Assume loanAmount = $100,000
Assume interestRate = 3.25%
Assume loanTerm = 15 years
Then formula for mortgage calculation is:
                monthlyRate = (interestRate / 100) / 12
                numPayments = loanTerm * 12
                monthlyPayment = loanAmount * monthlyRate \
                          * pow((1 + monthlyRate), numPayments) \
                          / (pow((1 + monthlyRate),numPayments) - 1)
                totalPayment = monthlyPayment * (loanTerm * 12)
                interestPaid = totalPayment - loanAmount

monthlyPayment would be:  $702.67
totalPayment would be: $126,480.28
interestPaid would be: $26,480.38

"""
def mortgage():       
    loop = True    

    while loop:  #  "While" Loop is used to repeat a specific block of code an unknown number of times, until a condition is met.
        p = float(input('\nEnter the loan amount, 0 to quit: '))
        if p > 0:
            r = float(input('Enter the loan interest rate %: '))
            n = int(input('Enter the loan term (number of years): '))
            monthlyrate = r/100/12
            numpayments = n*12
            monthlypayment = p*monthlyrate*pow((1+monthlyrate),numpayments)/(pow((1+monthlyrate),numpayments) - 1)
            totalpayment = monthlypayment*(n*12)           
            interestpaid = totalpayment - p      
            print('For the loan amount of ${:,.2f} for {} years with interest rate of {:.2f}%'.format(p, n, r))
            print('The monthly payment is ${:,.2f}'.format(monthlypayment)) 
            print('Total amount paid for this loan is ${:,.2f}'.format(totalpayment)) 
            print('Total interest paid for this loan is ${:,.2f}'.format(interestpaid))
        else:                 
            loop = False
            print("\nExisting mortgage progam....\n") 

                          
def sign():
    mortgage()
    
if __name__ == "__main__":
    mortgage()
    



 


 
