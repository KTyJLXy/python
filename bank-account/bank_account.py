import threading


class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.status = False
        self._lock = threading.Lock()

    def get_balance(self):
        if self.status == True:
            return self.balance
        else:
            raise ValueError("Invalid operation")

    def open(self):
        if self.status == True:
            raise ValueError("Invalid operation")
        else:
            self.status = True

    def deposit(self, amount):
        with self._lock:
            if self.status == True and amount >=0:
                self.balance += amount
            else:
                raise ValueError("Invalid operation")

    def withdraw(self, amount):
        with self._lock:
            if self.status == True and self.get_balance() >= amount and amount >= 0:
                self.balance -= amount
            else:
                raise ValueError("Invalid operation")

    def close(self):
        if self.status == False:
            raise ValueError("Invalid operation")
        else:
            self.status = False
            self.balance = 0
