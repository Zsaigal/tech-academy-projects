from abc import ABC, abstractmethod

# Parent abstract class defining the purchase process
class Purchase(ABC):
    # Abstract method for generating payslip
    @abstractmethod
    def payslip(self, amount):
        pass

    # Abstract method for payment
    @abstractmethod
    def payment(self, amount):
        pass

# Child class implementing the purchase process using a credit card payment method
class CreditCardPayment(Purchase):
    # Implementation of the payslip method
    def payslip(self, amount):
        print("Your purchase amount: ", amount)

    # Implementation of the payment method
    def payment(self, amount):
        print("Your purchase amount of {} is exceeding your limit of $400.".format(amount))

# Creating an object of the CreditCardPayment class and utilizing its methods
def main():
    obj = CreditCardPayment()
    obj.payslip("$500")  # Displaying the purchase amount
    obj.payment("500")   # Notifying about exceeding the credit card limit

if __name__ == "__main__":
    main()
