from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base
from sqlalchemy.orm import relationship


class Buzzsprout(Base):
  __tablename__ = 'buzzsprout'
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, unique=True, index=True)
  author = Column(String)
  description = Column(String)
  website_address = Column(String)
  contact_email = Column(String)
  keywords = Column(String)
  explicit = Column(String)
  main_category = Column(String)
  sub_category = Column(String)
  main_category2 = Column(String)
  sub_category2 = Column(String)
  main_category3 = Column(String)
  sub_category3 = Column(String)
  language = Column(String)
  timezone = Column(String)
  artwork_url = Column(String)
  background_url = Column(String)
  last_update = Column(String)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)