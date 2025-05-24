from implementation.mixins import CloneMixin


class PrototypeCloneCounter(CloneMixin):
    """Counts created and cloned objects."""

    _prototype_count = 0
    _clone_count = 0

    def __init__(self):
        PrototypeCloneCounter._prototype_count += 1

    @property
    def prototype_count(self) -> int:
        return self._prototype_count

    @property
    def clone_count(self) -> int:
        return self._clone_count

    def __deepcopy__(self, memo):
        if copied := memo.get(id(self)):
            return copied

        PrototypeCloneCounter._clone_count += 1

        new_copy = type(self).__new__(type(self))
        memo[id(self)] = new_copy
        new_copy._prototype_count = self._prototype_count
        new_copy._clone_count = self._clone_count

        return new_copy

    def __str__(self):
        return f"Prototypes: {self.prototype_count} Clones: {self.clone_count}"
