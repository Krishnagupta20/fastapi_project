from sqlalchemy import Column, Integer, String, Text
from fastapi_project.db import Base

class QueryResponse(Base):
    __tablename__ = "query_responses"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, index=True)
    response = Column(Text)
