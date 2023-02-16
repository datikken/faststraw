from sqlalchemy import create_engine
# from sqlalchemy import text


SQLALCHEMY_DATABASE_URL = "mysql://root:toor@127.0.0.1:3306/cointelegraph"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

connection = engine.connect()

# with engine.connect() as connection:
#     result = connection.execute(text("select * from podcasts"))
#     for row in result:
#         print(row)
        