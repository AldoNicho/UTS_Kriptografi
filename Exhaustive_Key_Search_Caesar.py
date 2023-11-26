alphabet = "abcdefghijklmnopqrstuvwxyz" 

def encrypt(text, key):
  encrypted = ""
  for char in text:
    if char in alphabet:
      idx = alphabet.index(char) 
      shifted_idx = (idx + key) % 26
      encrypted += alphabet[shifted_idx]
    else:
      encrypted += char
  
  return encrypted

def decrypt(ciphertext, key):
  return encrypt(ciphertext, -key)

def exhaustive_key_search(ciphertext):
  results = []
  
  for key in range(1, 26):
    decrypted = decrypt(ciphertext, key)
    print(f"Key {key}: {decrypted}")
    results.append(decrypted)
  
  return results
  
plaintext = "saya suka makan" 
key = 3
encrypted = encrypt(plaintext, key)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")

print("Exhaustive Key Search:")
exhaustive_key_search(encrypted)
