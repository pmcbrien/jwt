import jwt

# Example secret key
secret_key = "secret_key"

# Data to be encoded in the JWT
data = {"user_id": 12345}

# Encode the data with the secret key
encoded_jwt = jwt.encode(data, secret_key, algorithm='HS256')
print("Encoded JWT: ", encoded_jwt)

# Decode the JWT with the secret key
decoded_data = jwt.decode(encoded_jwt, secret_key, algorithms=['HS256'])
print("Decoded Data: ", decoded_data)
