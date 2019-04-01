import sys


from pony.orm import Database, Required, Optional, PrimaryKey, db_session
from datetime import datetime, date

from utils import DicoMixin

db = Database()



class Album(db.Entity, DicoMixin):
    _table_ = "albums"
    id = PrimaryKey(str, column="id")
    name = Required(str)
    year = Required(int)
    # owner_id =  char(36) COLLATE utf8_unicode_ci DEFAULT NULL,
    slug = Required(str)
    description = Optional(str)
    lat = Optional(float)
    lng = Optional(float)
    # cover_id =  char(36) COLLATE utf8_unicode_ci DEFAULT NULL,
    # options =  text COLLATE utf8_unicode_ci,
    created = Required(datetime, default=datetime.now)
    modified = Optional(datetime)
    active = Required(int, default=1)
    private = Required(int, default=0)
    views = Required(int, default=0)


db.bind(provider="mysql", host="localhost", user="k", passwd="k", db="knss")
db.generate_mapping(create_tables=True)



from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
import uvicorn

app = Starlette(debug=True)


@app.route("/")
async def homepage(request):
    return JSONResponse({"hello": "world"})


@app.route("/albums")
def albums(requests):
    with db_session:
        for i in Album.select()[:]:
            res = [i.dico for i in Album.select()[:]]
            return JSONResponse({"albums": res})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
