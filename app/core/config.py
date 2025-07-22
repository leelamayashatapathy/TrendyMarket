SECRET_KEY = "b1e2f3a4c5d6e7f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1d2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

demo_users_db = {
    "testuser": {
        "username": "testuser",
        "password": "testpass"
    }
}
rate_limit = {}
session = {}

ALLOWED_SECTORS = [
    "pharmaceuticals", "technology", "finance", "energy", "fmcg", "it", "banking", "auto", "telecom",
    "realty", "metals", "oil & gas", "healthcare", "infrastructure", "consumer durables", "power",
    "capital goods", "media", "chemicals", "insurance", "retail"
] 