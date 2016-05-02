import sys,datetime
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
 
Base = declarative_base()
Now = datetime.datetime.now()
 
class TagMapper(Base):
    __tablename__='tag'
    name=Column(String(50),nullable=False)
    id=Column(Integer, primary_key=True)
    status=Column(Integer,nullable=False,default=1)
 
class ArticleMapper(Base):
     
    __tablename__='article'
    title=Column(String(150),nullable=False)
    description=Column(String(150),nullable = False)
    status=Column(Integer,nullable=False,default=1)
    date_creation=Column(String(50),default=Now.strftime("%Y-%m-%d %H:%M"))
    date_update=Column(String(50),default=Now.strftime("%Y-%m-%d %H:%M"))
    id=Column(Integer, primary_key=True)
    #tag_id=Column(Integer, ForeignKey('tag.id'))
    #tag=relationship(Tag)
 
engine=create_engine("sqlite:///database.db",echo=True);
Base.metadata.create_all(engine)
