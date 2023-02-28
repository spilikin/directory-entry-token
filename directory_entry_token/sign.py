from jwcrypto import jwk, jwt
from time import time

key1 = jwk.JWK.from_json(open("key1.private.jwk").read())

claims = {
  "app": "oci",
  "v": "1",
  "sub": "1-20802376487",
  "name": "Praxis Dr.med. Carina Meyer",
  "mail": "carina.meyer@praxis.kim.telematik",
}

claims['iat'] = int(time())

entry_token = jwt.JWT(header={"alg": "ES256", "kid": key1.get('kid')}, claims=claims)
entry_token.make_signed_token(key1)

print(entry_token.serialize())
