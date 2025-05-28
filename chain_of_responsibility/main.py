from typing import Sequence

from implementation.topic import FilteredTopic, Topic, TopicType


def get_topic(
    name: str,
    topic_type: TopicType,
    messages: Sequence[str] = (),
    parent: Topic | None = None,
):
    topic = FilteredTopic(name, topic_type)

    if parent:
        topic.parent = parent

    for msg in messages:
        topic.append(msg)

    return topic


if __name__ == "__main__":
    sport_topic = get_topic("sport", TopicType.ARTICLE, ["Sport has no borders"])
    football_topic = get_topic(
        "football",
        TopicType.ARTICLE,
        ["Football is cool", "Soccer is cool too"],
        sport_topic,
    )
    team_topic = get_topic(
        "team", TopicType.EXCERPT, ["MU", "Inter", "Barcelona"], football_topic
    )
    hockey_topic = get_topic("hockey", TopicType.ARTICLE, ["Yikes!"], sport_topic)

    print("Only team messages:")
    team_messages = team_topic.all_filtered(name="team")
    assert team_messages == team_topic.all()
    print(team_messages, end="\n\n")

    print("Only articles:")
    article_messages = team_topic.all_filtered(topic_type=TopicType.ARTICLE)
    assert article_messages == football_topic.all() + "\n" + sport_topic.all()
    print(article_messages, end="\n\n")
    # nonexistent articles
    note_messages = team_topic.all_filtered(topic_type=TopicType.NOTE)
    assert not note_messages
    wrong_name_messsages = hockey_topic.all_filtered(name="tennis")
    assert not wrong_name_messsages
