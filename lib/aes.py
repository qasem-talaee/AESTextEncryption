from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
import base64
import random

class AESEncryption:
    def encypt(self, text, key):
        aes_key = PBKDF2(key, b'$G$GDFgbfd*#!kDFgbf$GDFgbfd*#!kd*#!k', dkLen=32, count=10000000)
        cipher = AES.new(aes_key, AES.MODE_CBC)
        padded_text = pad(text.encode(), AES.block_size)
        cipher_text = cipher.encrypt(padded_text)
        return base64.b64encode(cipher.iv).decode('utf-8'), base64.b64encode(cipher_text).decode('utf-8')

    def decrypt(self, iv, cipher_text, key):
        aes_key = PBKDF2(key, b'$G$GDFgbfd*#!kDFgbf$GDFgbfd*#!kd*#!k', dkLen=32, count=10000000)
        iv = base64.b64decode(iv)
        cipher_text = base64.b64decode(cipher_text)
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        padded_text = cipher.decrypt(cipher_text)
        return unpad(padded_text, AES.block_size).decode('utf-8')
    
    def GenerateKey(self):
        character_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+=|}][?/><:;abcdefghijklmnopqrstuvwxyz"
        key = ""
        for _ in range(1000):
            key += random.choice(character_list)
        return key