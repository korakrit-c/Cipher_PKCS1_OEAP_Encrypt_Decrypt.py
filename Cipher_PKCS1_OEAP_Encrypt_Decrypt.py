from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as Cipher_PKCS1_OAEP
from Crypto.Hash import SHA256
from base64 import urlsafe_b64decode, urlsafe_b64encode

def importKey(externKey):
    return RSA.importKey(externKey)

def encrypt_key(a_message, base64PublicKey):
    cipher = Cipher_PKCS1_OAEP.new(base64PublicKey, SHA256)

    #encoded_encrypted_msg = urlsafe_b64encode(cipher.encrypt(a_message))
    #return encoded_encrypted_msg.decode('ascii').rstrip("=")
    return cipher.encrypt(a_message)

def decrypt_key(ciphertext, base64PublicKey):
    cipher = Cipher_PKCS1_OAEP.new(base64PublicKey, SHA256)

    return cipher.decrypt(ciphertext)

def main():

    # https://8gwifi.org/RSAFunctionality?keysize=2048
    publicKeyStr = b'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzYBjJOJB3++Qdj3aKJ+/rMJE/vdf/roZj/PcEPhgL6OxY4P0GWfQTJm3RsEp2ZYhyFYZqQDWJtfAHRz3liivK8KnXKnbo4xrAcHIs4He+FJ3F7pS1E+8Wz4RFoIPRk7l8fRKvHiqhtRiE3Q3tsavvmRW0nAZy+plxi3JZuxwlDkTT50OCwB/jMIg5zHah06sc0fn60AttlNU0qFlxEe7DbwBhui2EkLG0ar8+QBfLnVBbisxxIIvCVQ8VVLncbGhP6yFd9wLIipkGzZpCCITjTkFFG+ZIqasbqTYjhQLz4w2+SNSYqn3DzVqdutygt/jdlQo05dRwStQvviiXNjTzwIDAQAB'
    privateKeyStr = b'MIIEowIBAAKCAQEAzYBjJOJB3++Qdj3aKJ+/rMJE/vdf/roZj/PcEPhgL6OxY4P0GWfQTJm3RsEp2ZYhyFYZqQDWJtfAHRz3liivK8KnXKnbo4xrAcHIs4He+FJ3F7pS1E+8Wz4RFoIPRk7l8fRKvHiqhtRiE3Q3tsavvmRW0nAZy+plxi3JZuxwlDkTT50OCwB/jMIg5zHah06sc0fn60AttlNU0qFlxEe7DbwBhui2EkLG0ar8+QBfLnVBbisxxIIvCVQ8VVLncbGhP6yFd9wLIipkGzZpCCITjTkFFG+ZIqasbqTYjhQLz4w2+SNSYqn3DzVqdutygt/jdlQo05dRwStQvviiXNjTzwIDAQABAoIBAC3SQ8kUniWlkCudTQij3iRSSPolBIWSz2JWuKocB653rHUJFiOYD00VNVWUepVmsW+vKxeQ9S9CCjczn00fEzgJtjGmOjA0fiOtJuhHvATYtm9W/2MRyGj75OmE5I0DyKfzlbqCmVto/dlin42krckhLG7NyiK6yCixSuglLlEOJqCq4n2tZTXBDOHhTTCYrR7WhdjeUW9bQYEYfjvFp9JCJadgnKx/ZBBbb4GLUAo3MpvIYlSMRR7Oqzvj7U8CikOFVH62dr3S/Lat58kanYf+T8WUNVuCxMJWLCM8Y8Xsf7oR/kOQTShBSgjEiKyXXOZCOEbxRIqt9D+URqKUCAkCgYEA6P8rwOVQ5pPgKlkMxmJVbiqz/jYjTQNvRoO4/yQxROD98MJYNRLesTF6kukmj0fbusr5+i6FKJS8Kb3oDQxiT6lsgCbuiu7Vjsdtz42gNBgkgxBzHFr3PlN46peRaQSF9Wny1Ij5Qbt3IdwSPYQ9YNuhaesPmV65ndNhHeEJ5VUCgYEA4cpLFyUXoBCLuaTl+azwLHDFlXQUp/qnE29estOqIignMkoRxen/4q+YxnkfoZb5Kc52pDzcSeagaSipZCVekpj4+3zHEw3mFqkAP4Um0T0yyMH+buAIs02OcjQ8nRyNLF6Lh7ia64UjV/e9ailctRCLSMt1CXG6rs/DWG1BlJMCgYEAhtHwXWPT1jhHA/oXPEv2JxMqp7Rn5M5R+zmJOImWwMZ36nJqW/uZRGrfBFdI6qun54Q/9ZYpkvvNjVHIDpTV5kag896TNW1RwZaAYhMPWlWF+xjvor64RiZC12vwxhXJ9eHikzzXDkQNgVg4bcQxR/SOiB1uH08ClOKVVZa8BSkCgYAgD7Od87xpFDBjChFF5NKt3M2RrUwJlkQHNHdD+V5dP0phj7b6XYHiVIDjHevp7CAxWYnrRGEbdU4t4II9IDlPo70nKM6z2/NiIFlSq7uZVpFRhIp2gAV8QHULrnM09Arv0/UILqSA8QTVxu30ly783v6INavGzYlurT3V3p3DVQKBgAgWZ92al2TkpJuUx+hCoxn6BtpMOS4qExbwdS3/t044Sb5ldc/Srrddx/jF5KoUoaq0y6SK4rbJnUwYMA31nGjDDuVAwPhCkww7njEApkqAmRX+tzDl92I1QhU71Rlfd9O+uiu85gy+lARSonzXdFB5oDtw1hQwjbgGyfjghATG'
    message = b'Hello Arthur'

    encoded = encrypt_key(message, importKey(urlsafe_b64decode(publicKeyStr)))
    print(encoded)

    decoded = decrypt_key(encoded, importKey(urlsafe_b64decode(privateKeyStr)))
    print(decoded)

if __name__== "__main__":
    main()
