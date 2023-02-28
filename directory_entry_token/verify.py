from jwcrypto import jwk, jwt
import sys

entry_token = sys.argv[1]

ks = jwk.JWKSet.from_json(open("jwks.json").read())

entry_token_jwt = jwt.JWT(key=ks, jwt=entry_token)

print(entry_token_jwt.claims)