Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'ZDK-03 AEW&C')
m.hexdigest()
'a171c9dd3a43b1fc42483143769c542f3221f2d73bba80574bcd854b066e9442'
