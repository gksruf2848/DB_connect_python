import jaydebeapi

query = '''CREATE TABLE IF NOT EXISTS exoplanets (
          id INT PRIMARY KEY AUTO_INCREMENT,
          name VARCHAR NOT NULL,
          year_discovered SIGNED,
          light_years FLOAT,
          mass FLOAT,
          link VARCHAR)'''

connection  = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:tcp://localhost:9092/inbodydb",
    ["SA", ""],
    "/Users/hanlim_air/HANLIM/h2/bin/h2-1.4.200.jar")
cursor = connection.cursor()
returnResult = None
cursor.execute(query, returnResult)
if returnResult:
    #returnResult = _convert_to_schema(cursor)
    print('okay')
cursor.close()
connection.close()