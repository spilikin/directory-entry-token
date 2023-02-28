from jwcrypto import jwk

key1 = jwk.JWK.generate(kty='EC', crv='P-256', kid='key1')
key2 = jwk.JWK.generate(kty='EC', crv='P-256', kid='key2')

open('key1.private.jwk', 'w').write(key1.export_private())
open('key2.private.jwk', 'w').write(key2.export_private())

ks = jwk.JWKSet()
ks.add(key1)
ks.add(key2)

open('jwks.json', 'w').write(ks.export(private_keys=False))
