from abc import abstractmethod


class Parent:
    def do_this(self):
        self._on_do_this()
        # default implementaion
        print("Do this.")

    def _on_do_this(self): ...

    def do_that(self):
        self._on_do_that()
        self._to_do()
        self._on_after_do_that()

    def _on_do_that(self): ...

    @abstractmethod
    def _to_do(self): ...

    def _on_after_do_that(self): ...
