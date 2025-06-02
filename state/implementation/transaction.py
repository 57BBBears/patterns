from interfaces.state import Transaction, TransactionState


class DataTransaction(Transaction):
    def __init__(self, state: TransactionState):
        self._state = state

    def open(self):
        self._state.open(self)

    def transfer(self, data: dict):
        self._state.transfer(data, self)

    def commit(self):
        self._state.commit(self)

    def close(self):
        self._state.close(self)

    def set_state(self, state: TransactionState):
        self._state = state
