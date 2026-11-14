class Application:
    def payment(self):
        print("Payment is done.")


class GooglePay(Application):    #here google pay parent is application
    def payment(self):
            print("Payment is done through google pay.")
    
class PhonePay(Application):    #here phone pay parent is Application
    def payment(self):
            print("Payment is done through Phone pay.")

g=GooglePay()
p=PhonePay()

p.payment()
g.payment()


# Payment is done through Phone pay.
# Payment is done through google pay.





print("To access and achieve super class of each child in hierarchial inheritance")
print("+=================================================================================+")
class Application:
    def payment(self):
        print("Payment is done.")


class GooglePay(Application):
    def payment(self):
            print("Payment is done through google pay.")
            super().payment()  #here google pay parent is application
    
class PhonePay(GooglePay):
    def payment(self):
            print("Payment is done through Phone pay.")
            super().payment() #here phone pay parent is google pay
g=GooglePay()
p=PhonePay()

p.payment()
g.payment()

# Payment is done through Phone pay.
# Payment is done through google pay.
# Payment is done.
# Payment is done through google pay.
# Payment is done.