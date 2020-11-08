from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import codecs

# key = RSA.generate(1024)
# private_key = key.exportKey()
# public_key = key.publickey().exportKey()

private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCYJSqyui0OT45/L5n1pJ14L9Z87ceS2/zLqPevRcypwkJZbq2M\nYtEqGFOZNj3uZm5ZaEtapVUD9jxTagEhL5YOCQ6vLcz0sYhlKXmdcoKQd4VYJqdl\nkrke610D9CENxYlLq73WckT1MtbgZW4jzCo66r7IeZmcXu3p1NtoMlQjHQIDAQAB\nAoGAZWwhUpOZhXizXUW2NHJQJtZ8/TrlV5kepAU3V7gH/wJoiIWnW3ZkSNN+pxvp\nnQrbdO55jSu5yLJU9KYtqpm2RQz+xdoU88Eo7raKvL3gJ4odT8D7CFGWozBgJ0kU\nlwZfBKhJavScSMWLwxPVxSD6jYGwIu9N4qiYW2BLbaw9mmECQQC2PROppdhwd4xZ\nNQ2sidu2nVhNBSeoPHcq9qAx88ZACzVesq3udh1Vtmg6FUFHJH6LmJ7wTJOd84IQ\nszGtxRiXAkEA1bnq4BxXVNIgBis6c7gTnvwxXPgdTwvK0m2oYWX0P7/uyXf9WhdU\n7FXoEbM2fDYTZiXOmLgLe0zLGLtT3YOEawJADjy3TImoXyD31gBPESuz/pBMVbgR\nYRNYPAMIgN6KnnZBtSRAcmDH6epWOjNu5h/zwvQpdpyE69IaVzOoreq4AQJARxpa\nHILxPuPFCahaAuOLi4nlNkPJJGIM8OLQcM7FamwFGfuUSuOWOiX+Vd0kVEB9Ra9w\nQvh/wV5z9t9jcD9vzwJAGllGQoE+Ay7or/Ur6JPAdTkBABnxJ2YELqGIfR8+i2Um\nEW2qzACWn7UHszrk0woAHUmA2UA52cenWBGz+dHMqw==\n-----END RSA PRIVATE KEY-----'
public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYJSqyui0OT45/L5n1pJ14L9Z8\n7ceS2/zLqPevRcypwkJZbq2MYtEqGFOZNj3uZm5ZaEtapVUD9jxTagEhL5YOCQ6v\nLcz0sYhlKXmdcoKQd4VYJqdlkrke610D9CENxYlLq73WckT1MtbgZW4jzCo66r7I\neZmcXu3p1NtoMlQjHQIDAQAB\n-----END PUBLIC KEY-----'

# print(private_key)
# print(public_key)

message = "Hello World".encode('utf-8')
h = SHA256.new(message)

priv_key = RSA.importKey(private_key)
pub_key = RSA.importKey(public_key)

singer = PKCS1_v1_5.new(priv_key)
signature = singer.sign(h)
print(signature)
hexify = codecs.getencoder('hex')
m = hexify(signature)[0]
print(m)
