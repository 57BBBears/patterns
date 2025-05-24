import copy


class CloneMixin:
    def clone(self):
        return copy.deepcopy(self)
