class CreditCardPayment:

    def process_payment(self, amount):
        print(f"\nProcessing credit card payment of ${amount}")

class PayPalPayment:
    
    def process_payment(self, amount):
        print(f"\nProcessing PayPal payment of ${amount}")

class BankTransferPayment:
    def process_payment(self, amount):
        print(f"\nProcessing bank transfer payment of ${amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

if __name__ == "__main__":
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()
payment = [credit_card, paypal, bank_transfer]
amounts = [100, 200, 300]

for method, amt in zip(payment, amounts):
    make_payment(method, amt)
