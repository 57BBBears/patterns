from implementation.states import ClosedTransaction, OpenedTransaction
from implementation.transaction import DataTransaction

if __name__ == "__main__":
    transaction = DataTransaction(ClosedTransaction())
    transaction.open()
    transaction.transfer({"some": "data"})
    transaction.commit()
    transaction.transfer({"another": "data"})
    transaction.set_state(OpenedTransaction())
    transaction.transfer({"another": "data"})
    transaction.close()
    transaction.commit()
