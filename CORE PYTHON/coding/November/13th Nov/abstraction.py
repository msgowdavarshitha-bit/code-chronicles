from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def transaction(self):
        self

class GooglePay(Payment):    #here google pay parent is application
    def transaction(self):
            print("Payment is done through google pay.")
    
class PhonePay(Payment):    #here phone pay parent is Application
    def transaction(self):
            print("Payment is done through Phone pay.")

g=GooglePay()
p=PhonePay()

p.transaction()
g.transaction()


# Payment is done through Phone pay.
# Payment is done through google pay.

#we should not create object for the abstract class