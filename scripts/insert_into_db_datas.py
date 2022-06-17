import random
import time
from functools import wraps

from models.job import Job
from utils.common import (gen_random_string,
                          gen_uuid_str)
from schemas.job import JobSchema
from mongoengine.context_managers import switch_db


def time_record(func):
    # @wraps
    def _deco(*args, **kwargs):
        start_time = time.time()
        r = func(*args, **kwargs)
        cost = time.time() - start_time
        print("func [{}] cost {}\n".format(func.__name__, cost))
        return r
    return _deco



def get_tags():
    tags = []
    element_count = random.randint(1, 10)
    element_len = random.randint(5, 10)
    for i in range(element_count):
        tags.append(gen_random_string(element_len))

    return tags


def get_job_context():
    res = {
        "id": random.randint(1, 10000000),
        "name": gen_random_string(15)
    }
    return res


def gen_datas(count=10000):
    datas = []
    for i in range(count):
        payload = {
            "display_name": gen_random_string(16),
            "description": "",
            "min_replica_count": 10,
            "max_replica_count": 1,
            "status": "success",
            "tags": get_tags(),
            "timeout_in_minute": random.randint(30, 100),
            "job_context": get_job_context(),
            "project_id": gen_uuid_str(),
            "creator": random.randint(1, 1000000),
        }

        # insert(payload)
        datas.append(payload)

    return datas


@time_record
def insert_without_index_db(count=10000):
    datas = gen_datas(count)
    with switch_db(Job, "without_index") as Jobs:
        for item in datas:
            Jobs.objects.create(**item)


@time_record
def insert_data_to_db(count=10000):
    datas = gen_datas(count)
    for data in datas:
        Job.objects.create(**data)


def test_pydantic():
    payload = {
        "display_name": gen_random_string(16),
        "description": "",
        "min_replica_count": 10,
        "max_replica_count": 1,
        "status": "success",
        "tags": get_tags(),
        "timeout_in_minute": random.randint(30, 100),
        "job_context": get_job_context(),
        "project_id": gen_uuid_str(),
        "creator": random.randint(1, 1000000),
        "user_id": "test-mj",
        "worker":4
    }

    job = JobSchema(**payload)
    print(job)


if __name__ == "__main__":
    insert_data_to_db(count=300000)
    print("insert data to db with index success !!! ")

    insert_without_index_db(count=300000)
    print("insert data to db without index success !!!")




