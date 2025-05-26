from implementation.connectors import DummyConnector, QueueConnector
from implementation.entities import ConnectorEntityError, Entity, VerboseEntity

if __name__ == "__main__":
    # connector is not set error
    try:
        error_entity = Entity("error", "")
        error_entity.get_data()
    except ConnectorEntityError as e:
        print(e)

    # Base Entity and Dummy connector
    Entity.connector = DummyConnector()
    entity = Entity("test", "test")
    entity.get_data()
    print(entity)

    # Verbose Entities and Queue connector
    VerboseEntity.connector = QueueConnector()
    queue_entity = VerboseEntity("queue", "queue")
    queue_entity.get_data()
    queue_entity1 = VerboseEntity("one more", "one more")
    queue_entity1.get_data()
    print(queue_entity1)
