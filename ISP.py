from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass


class OnlinePaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")


class NoRefundProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")


def main():
    online = OnlinePaymentProcessor()
    no_refund = NoRefundProcessor()

    online.process_payment(10000)
    online.process_refund(8000)

    no_refund.process_payment(5000)
    # no_refund.process_refund(200)


if __name__ == '__main__':
    main()
