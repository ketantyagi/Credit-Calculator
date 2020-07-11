import math
import sys


class Credit:
    def annuity_payment(self, principal, i, n):
        self.i = (i / 100) / 12
        payment = round(principal * (self.i * math.pow(1 + self.i, n) / (math.pow(1 + self.i, n) - 1)), 2)
        return math.ceil(payment)

    def credit_principal(self, annuity_payment, interest, period):
        self.i = (interest / 100) / 12
        principal = annuity_payment / (self.i * math.pow(1 + self.i, period) / (math.pow(1 + self.i, period) - 1))
        return math.floor(principal)

    def period(self, annuity_payment, principal, i):
        self.i = (i / 100) / 12
        months = math.ceil(math.log(annuity_payment / (annuity_payment - (self.i * principal)), 1 + self.i))
        return months

    def diff_payment(self, principal, interest, period):
        payment = 0
        payments = []
        total_payment = 0.0
        interest = (interest / 100) / 12
        for number in range(0, period):
            payment = math.ceil(
                (principal / period) + interest * (principal - ((principal * (number + 1 - 1)) / period)))
            payments.append(payment)
            print("Month {}: paid out {}".format(number + 1, payments[number]))
            total_payment += payment
        print("\nOverpayment =", math.ceil(total_payment - principal))


result = Credit()
args = sys.argv
if len(args) != 5:
    print("Incorrect parameters.")
if len(args) == 5:
    if args[1].find("diff") != -1:
        principal = float(args[2][args[2].find('=')+1:])
        period = int(args[3][args[3].find('=')+1:])
        interest = float(args[4][args[4].find('=') + 1:])
        result.diff_payment(principal, interest, period)

    elif args[1].find("annuity") != -1:
        if args[2].find("principal") != -1 and args[3].find("period") != -1 and args[4].find("interest") != -1:
            principal = float(args[2][args[2].find('=') + 1:])
            period = int(args[3][args[3].find('=') + 1:])
            interest = float(args[4][args[4].find('=') + 1:])
            if principal < 0 or period < 0 or interest < 0:
                print("Incorrect parameters")
            else:
                print("Your annuity payment = {}!".format(result.annuity_payment(principal, interest, period)))
                print("Overpayment = {}".format(int((result.annuity_payment(principal, interest, period) * period)- principal)))

        elif args[2].find("payment") != -1 and args[3].find("period") != -1 and args[4].find("interest") != -1:
            payment = int(args[2][args[2].find('=') + 1:])
            period = int(args[3][args[3].find('=') + 1:])
            interest = float(args[4][args[4].find('=') + 1:])
            if payment < 0 or period < 0 or interest < 0:
                print("Incorrect parameters.")
            else:
                print("Your credit principal = {}!".format(result.credit_principal(payment, interest, period)))
                print("Overpayment = {}".format(int((payment * period) - result.credit_principal(payment,interest, period))))

        elif args[2].find("principal") != -1 and args[3].find("payment") != -1 and args[4].find("interest") != -1:
            principal = float(args[2][args[2].find('=') + 1:])
            payment = float(args[3][args[3].find('=') + 1:])
            interest = float(args[4][args[4].find('=') + 1:])
            if principal < 0 or payment < 0 or interest <0:
                print("Incorrect parameters.")
            else:
                months = result.period(payment, principal, interest)
                if months < 12:
                    print("You need {} months to repay this credit!".format(months))
                elif months == 12:
                    print("You need 1 year to repay this credit!")
                elif months > 12 and months % 12 == 0:
                    print("You need {} years to repay this credit!".format(months // 12))
                elif months > 12 and months % 12 != 0:
                    print(f"You need {months // 12} years and {months % 12} months to repay this credit!")
                print("Overpayment = {}".format(int((payment * months) - principal)))