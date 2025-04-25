from PIL import Image

# Open the .jpg image
img = Image.open("assets/icon.jpg")

# Resize the image to 256x256 pixels (standard size for icons)
size = (256, 256)
img = img.resize(size, Image.LANCZOS)

# Save the image as an .ico file
img.save("assets/icon.ico", format="ICO", sizes=[size])

print("Conversion complete! The .ico file is saved as 'assets/icon.ico'.")
