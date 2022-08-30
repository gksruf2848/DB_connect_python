import jaydebeapi
from marshmallow import Schema, fields, EXCLUDE

def initialize():
    _execute(
        ("CREATE TABLE IF NOT EXISTS exoplanets ("
         "  id INT PRIMARY KEY AUTO_INCREMENT,"
         "  name VARCHAR NOT NULL,"
         "  year_discovered SIGNED,"
         "  light_years FLOAT,"
         "  mass FLOAT,"
         "  link VARCHAR)"))

def _execute(query, returnResult=None):
    connection  = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:tcp://localhost:9092/exoplanets",
        ["SA", ""],
        "/Users/hanlim_air/HANLIM/h2/bin/h2-1.4.200.jar")
    cursor = connection.cursor()
    cursor.execute(query)
    if returnResult:
        returnResult = _convert_to_schema(cursor)
    cursor.close()
    connection.close()

    return returnResult

class ExoplanetSchema(Schema):
    id = fields.Integer(allow_none=True)
    name = fields.Str(required=True, error_messages={"required": "An exoplanet needs at least a name"})
    year_discovered = fields.Integer(allow_none=True)
    light_years = fields.Float(allow_none=True)
    mass = fields.Float(allow_none=True)
    link = fields.Url(allow_none=True)
    class Meta:
        unknown = EXCLUDE

def _convert_to_schema(cursor):
    column_names = [record[0].lower() for record in cursor.description]
    column_and_values = [dict(zip(column_names, record)) for record in cursor.fetchall()]

    return ExoplanetSchema().load(column_and_values, many=True)

