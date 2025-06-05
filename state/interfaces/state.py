from abc import ABC, abstractmethod


class Transaction(ABC):
    """Base transaction interface."""

    @abstractmethod
    def open(self): ...

    @abstractmethod
    def transfer(self, data: dict): ...

    @abstractmethod
    def commit(self): ...

    @abstractmethod
    def close(self): ...

    @abstractmethod
    def set_state(self, state: "TransactionState"): ...


class TransactionState(ABC):
    """Transaction states can be permanent - being created at once and initialised by a
    transaction or be temporary like here and accept transaction instance as needed."""

    @abstractmethod
    def open(self, transaction: Transaction): ...

    @abstractmethod
    def transfer(self, data: dict, transaction: Transaction): ...

    @abstractmethod
    def commit(self, transaction: Transaction): ...

    @abstractmethod
    def close(self, transaction: Transaction): ...

    @staticmethod
    def _set_state(transaction: Transaction, state: "TransactionState"):
        transaction.set_state(state)
