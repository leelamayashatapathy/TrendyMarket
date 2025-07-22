from app.core.config import session

def get_and_update_session(user: str, sector: str):
    seson = session.get(user, {"calls": 0, "last_sector": None})
    seson["calls"] += 1
    seson["last_sector"] = sector.lower()
    session[user] = seson
    return seson 