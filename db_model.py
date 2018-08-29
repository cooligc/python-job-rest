from data_store import Base
from sqlalchemy import Column,Integer, String

class JobEntity(Base):
    __tablename__ = 'JOBS'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    job_id = Column(String(255))
    status = Column(String(255))
    initiated_by = Column(String(255))

    def __init__(self, name, job_id, status, initiated_by):
        self.initiated_by = initiated_by
        self.name = name
        self.job_id = job_id
        self.status = status
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

