from PIL import Image

image = Image.open("car.jpeg")
pixels = image.load()
width,height = image.size
key = int(input("Enter the key:"))
def encrypt(image, key):
    pixels = image.load()
    width,height = image.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    return image

def decrypt(image, key):
    return encrypt(image, key)

encrypted_image = encrypt(image.copy(), key)
encrypted_image.save('encryptedImage.png')
decrypted_image = decrypt(encrypted_image, key)
decrypted_image.save('decryptedImage.png')
