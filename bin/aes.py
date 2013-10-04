from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from os import urandom

BLOCK_SIZE = 32

INTERRUPT = u'\u0001'
PAD = u'\u0000'

SECRET_KEY = u'12345678901234567890123456789012'
IV = urandom(16)

def AddPadding(data, interrupt, pad, block_size):
    new_data = ''.join([data, interrupt])
    new_data_len = len(new_data)
    remaining_len = block_size - new_data_len
    to_pad_len = remaining_len % block_size
    pad_string = pad * to_pad_len
    
    return ''.join([new_data, pad_string])

def StripPadding(data, interrupt, pad):
    return data.rstrip(pad).rstrip(interrupt)

def EncryptRunner(plaintext_data, encrypt_cipher=AES.new(SECRET_KEY, AES.MODE_CBC, IV)):
    plaintext_padded = AddPadding(plaintext_data, INTERRUPT, PAD, BLOCK_SIZE)
    encrypted = encrypt_cipher.encrypt(plaintext_padded)
    
    return b64encode(encrypted)

def DecryptRunner(encrypted_data, decrypt_cipher=AES.new(SECRET_KEY, AES.MODE_CBC, IV)):
    decoded_encrypted_data = b64decode(encrypted_data)
    decrypted_data = decrypt_cipher.decrypt(decoded_encrypted_data)
    
    return StripPadding(decrypted_data, INTERRUPT, PAD)
    
