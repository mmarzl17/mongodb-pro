import datetime
from mongoengine import (Document,
                         SequenceField,
                         StringField,
                         IntField,
                         ListField,
                         DictField,
                         DateTimeField
                         )


class Job(Document):
    """
    table of job in backend storage.
    """

    uuid = SequenceField(collection_name="counters")
    display_name = StringField(max_length=255, required=True)
    description = StringField(max_length=1000)
    min_replica_count = IntField(default=10)
    max_replica_count = IntField(default=1)
    status = StringField(max_length=255, required=True)
    tags = ListField()
    timeout_in_minute = IntField(default=30)
    job_context = DictField(default=dict())
    project_id = StringField(max_length=255, required=True)
    creator = IntField()
    create_time = DateTimeField(default=datetime.datetime.utcnow())