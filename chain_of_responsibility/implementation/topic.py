from enum import StrEnum, auto
from typing import Generic, TypeVar


class TopicType(StrEnum):
    ARTICLE = auto()
    EXCERPT = auto()
    NOTE = auto()


T = TypeVar("T", bound="Topic")


class Topic(Generic[T]):
    def __init__(self, name: str, topic_type: TopicType):
        self.name = name
        self.type = topic_type
        self.parent: T | None = None
        self._messages: list[str] = []

    def append(self, message: str):
        self._messages.append(message)

    def latest(self) -> str | None:
        if len(self._messages):
            return self._messages[-1]

        return None

    def all(self, sep: str = "\n") -> str:
        return sep.join(self._messages)


class FilteredTopic(Topic):
    """Implements chain of responsibility pattern.
    Extends Topic by filtering and getting messages from parent topics."""

    _filtered_messages: list[str] = []

    def get_by(
        self, *, topic_type: TopicType | None = None, name: str = ""
    ) -> list[str]:
        """Collects messages by topic name or type."""
        if topic_type:
            result = self._get_by_type(topic_type)
        elif name:
            result = self._get_by_name(name)
        else:
            result = []

        return result

    def _get_by_type(self, topic_type: TopicType) -> list[str]:
        """Goes through all parent topics and collects messages by the topic type."""
        if self.type is topic_type:
            FilteredTopic._filtered_messages.extend(self._messages)

        return self._handle_next(topic_type=topic_type)

    def _get_by_name(self, name: str):
        """Finds the topic by name and return its messages.
        Look up the name til the top parent."""
        if self.name == name:
            return self._messages

        return self._handle_next(name=name)

    def _handle_next(
        self, *, topic_type: TopicType | None = None, name: str = ""
    ) -> list[str]:
        if self.parent:
            return self.parent.get_by(topic_type=topic_type, name=name)
        # clear _filtered_messages for the next filter
        messages, FilteredTopic._filtered_messages = (
            self._filtered_messages.copy(),
            [],
        )

        return messages

    def all_filtered(
        self, topic_type: TopicType | None = None, name: str = "", sep: str = "\n"
    ) -> str:
        return sep.join(self.get_by(topic_type=topic_type, name=name))
