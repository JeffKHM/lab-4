# Program name    : Functions.
# Program purpose : Modify the mortgage.py program function that will calculate mortgage payment.And also using keyword "import" to add in calculateMenu.py
# Created/revised :on 4/18/2020 jeff
# This program calculates the ending principal in a bank
# account after compounding the interest.

def simpleInterest():
    #print("Lab3 - CNET 142: Program written by: Kee Hock Meng")  # change Ron S to your name
    loop = True

    while loop:
        print('\nEnter the starting principal, <= 0 to quit: ', end='') #print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。
        p = float(input())
        
        if p > 0:
            
            print('Enter the annual interest rate : ', end='')
            r = float(input())
           
            print('How many times per year is the interest compounded? ', end='')
            n = int(input())
            
            print('For how many years will the account earn interest? ', end='')
            t = float(input())

            # Adjust the interest rate.
            r = r / 100

            # Calculate the ending balance.
            a = p * (1 + float(r) / n) ** (n * t)
            interest = a - p

            # Display the ending balance.
            print('At the end of', t, 'years you will have $', format(a, ',.2f'), \
                  'with interest earned $', format(interest, ',.2f'))
        else:
            loop = False
            print('\nExisting Simple Interest program ...\n')
 
def sign():
    simpleInterest()


if __name__ == "__main__":
    simpleInterest()
    print("Have a nice day\n")
 
