from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from database.database import Base


class Podcast(Base):
  __tablename__ = 'podcasts'
  
  id = Column(Integer, primary_key=True, index=True)
  slug = Column(String, unique=True, index=True)
  title = Column(String)
  description = Column(String)
  buzzsprout_id = Column(Integer, ForeignKey('buzzsprout.id'))
  apple = Column(String)
  spotify = Column(String)
  google = Column(String)
  amazon_music = Column(String)
  audible = Column(String)
  iheartradio = Column(String)
  tunein = Column(String)
  podcast_addict = Column(String)
  podchaser = Column(String)
  podcast_index = Column(String)
  pocket_casts = Column(String)
  deezer = Column(String)
  listen_notes = Column(String)
  playerfm = Column(String)
  overcast = Column(String)
  castro = Column(String)
  castbox = Column(String)
  podfriend = Column(String)
  goodpods = Column(String)
  disclaimer_prefix = Column(String)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)