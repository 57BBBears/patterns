from interfaces.state import Transaction, TransactionState


class OpenedTransaction(TransactionState):
    def open(self, transaction: Transaction): ...

    def transfer(self, data: dict, transaction: Transaction):
        print(f"Transfering data {data} ...")

    def commit(self, transaction: Transaction):
        print("Data has commited.")
        self._set_state(transaction, CommitedTransaction())

    def close(self, transaction: Transaction):
        print("Closing transaction...")
        self._set_state(transaction, ClosedTransaction())


class CommitedTransaction(TransactionState):
    def open(self, transaction: Transaction): ...

    def transfer(self, data: dict, transaction: Transaction):
        print(f"Synchronizing data {data} ...")

    def commit(self, transaction: Transaction):
        print("Data has commited.")

    def close(self, transaction: Transaction):
        print("Closing transaction...")
        self._set_state(transaction, ClosedTransaction())


class ClosedTransaction(TransactionState):
    def open(self, transaction: Transaction):
        print("Opening transaction...")
        self._set_state(transaction, OpenedTransaction())

    def transfer(self, data: dict, transaction: Transaction): ...

    def commit(self, transaction: Transaction): ...

    def close(self, transaction: Transaction): ...
