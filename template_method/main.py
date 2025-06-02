from implementation.children import DefaultChild, YellingChild

if __name__ == "__main__":
    default_child = DefaultChild()
    default_child.do_this()
    default_child.do_that()

    yelling_child = YellingChild()
    yelling_child.do_this()
    yelling_child.do_that()
