from typing import List, Dict

from pydantic import BaseModel


class JobSchema(BaseModel):
    display_name: str
    description: str = None
    min_replica_count: int = 10
    max_replica_count: int = 1
    status: str
    tags: List = []
    timeout_in_minute: int = 30
    job_context: Dict = {}
    project_id: str
    creator: str