from implementation.dtos import BaseDTO, BooleanDTO, ColoredDTO
from implementation.prototypes import PrototypeCloneCounter
from implementation.repository import PrototypeRepository


class CounterApp:
    def __init__(self, prototype: PrototypeCloneCounter):
        self.copy = prototype.clone()


def test_single_prototype():
    print("Cloning a single prototype example.")

    proto = PrototypeCloneCounter()
    assert proto.prototype_count == 1
    assert proto.clone_count == 0
    print("Original ", proto)

    app = CounterApp(proto)
    clone = app.copy
    assert clone.prototype_count == 1
    assert clone.clone_count == 1
    print("Cloned ", clone)

    new_proto = PrototypeCloneCounter()
    assert proto.prototype_count == 2
    assert proto.clone_count == 1
    print("New ", new_proto)


def test_repository():
    print("Cloning prototypes by a repository example.")

    base_dto: BaseDTO = BaseDTO(name="base", value=1)
    colored_dto = ColoredDTO(name="colored", value=2, color="red")
    boolean_dto = BooleanDTO(name="boolean", value=3, is_true=True)
    prototypes = [base_dto, colored_dto, boolean_dto]

    repo = PrototypeRepository()
    for proto in prototypes:
        repo.add(proto.name, proto)

    base_clone = repo[base_dto.name]
    assert base_clone is not base_dto
    print(base_clone)

    colored_clone = repo.get_by_color(colored_dto.color)[0]
    assert colored_clone is not colored_dto
    print(colored_clone)

    boolean_clone = repo.get_true()[0]
    assert boolean_clone is not boolean_dto
    print(boolean_clone)


if __name__ == "__main__":
    test_single_prototype()

    test_repository()
