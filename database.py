import json
import logging
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class WhoisData(Base):
    __tablename__ = 'whois_data'
    id = Column(Integer, primary_key=True)
    domain_name = Column(String, unique=True, nullable=False)
    status = Column(Text, nullable=True)
    registrar = Column(String, nullable=True)
    registrant = Column(String, nullable=True)
    administrative_contact = Column(String, nullable=True)
    name_servers = Column(Text, nullable=True)
    created = Column(DateTime, nullable=True)
    last_modified = Column(DateTime, nullable=True)
    expiry_date = Column(DateTime, nullable=True)

DATABASE_URL = "sqlite:///whois_data.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def save_whois_data(whois_data):
    try:
        whois_record = WhoisData(
            domain_name=whois_data['domain_name'],
            status=','.join(whois_data.get('status', [])),
            registrar=whois_data.get('registrar'),
            registrant=whois_data.get('registrant'),
            administrative_contact=whois_data.get('administrative_contact'),
            name_servers=','.join(whois_data.get('name_servers', [])),
            created=datetime.fromisoformat(whois_data['created']) if whois_data['created'] else None,
            last_modified=datetime.fromisoformat(whois_data['last_modified']) if whois_data['last_modified'] else None,
            expiry_date=datetime.fromisoformat(whois_data['expiry_date']) if whois_data['expiry_date'] else None
        )
        session.add(whois_record)
        session.commit()
    except Exception as e:
        logging.error(f"Error saving whois data: {e}")
        session.rollback()
