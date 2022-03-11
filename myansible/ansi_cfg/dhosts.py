#!/usr/bin/python3
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
#create a database engine
engine = create_engine(
    'mysql+pymysql://root:Rxt123..@127.0.0.1/ansibledb?charset=utf8',encoding='utf8'
)
#create a base class from engine,use for ORM
Base = declarative_base(engine);

#create a obeject of session to update,insert,delete,select mysqldb
Session = sessionmaker(bind=engine);

class Groups(Base):
    __tablename__ = 'apis_groups';
    id = Column(Integer,primary_key=True);
    GroupName = Column(String(50));
class Hosts(Base):
    __tablename__ = 'apis_hosts';
    id = Column(Integer,primary_key=True);
    HostName = Column(String(200));
    HostIp = Column(String(15));
    Group_id = Column(ForeignKey('apis_groups.id'));

if __name__ == '__main__':
    #a real object
    session = Session();
    #generate an select object >> query_set
    query_set = session.query(Groups.GroupName,Hosts.HostIp).join(Hosts);
    res = {};
    for group,ip in query_set.all():
        if group not in res:
            res[group] = {};
            res[group]['hosts'] = [];
        res[group]['hosts'].append(ip);
    print(json.dumps(res));

