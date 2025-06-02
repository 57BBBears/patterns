from implementation.parent import Parent


class DefaultChild(Parent):
    def __init__(self):
        print("Default child.")

    def _to_do(self):
        print("Default doing.")


class YellingChild(Parent):
    def __init__(self):
        print("Yelling child.")

    def _on_do_this(self):
        print("BEFORE DOING THIS")

    def _on_do_that(self):
        print("BEFORE DOING THAT")

    def _to_do(self):
        print("DOING!")

    def _on_after_do_that(self):
        print("AFTER DOING THAT")
