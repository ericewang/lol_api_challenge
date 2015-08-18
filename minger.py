from ming import collection, Field, Session
from ming import schema as S
from ming.declarative import Document

session = Session()
"""
Champion = collection(
    'champion.name', session,
    Field('_id', S.ObjectId),
    Field('name', str)
)
"""
class Champion(Document):
    class __mongometa__:
        session=session
        name='champion.name'
        indexes=['champion.name']
    _id=Field(str)
    name=Field(str)
    data=Field([
