from .receipt import Receipt

mem = {}

def ingest(id, data):
    #Map to model
    r = Receipt(id, data["retailer"], data["purchaseDate"], data["purchaseTime"], data["items"], data["total"])
    mem[id] = r
    #Return id to build path
    return id

def score(id):
    r = mem[str(id)]
    points = r.get_points()

    return points