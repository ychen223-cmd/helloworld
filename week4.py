from PIL import Image, ImageDraw

# Create a white canvas
img = Image.new("RGB", (600, 400), "white")
draw = ImageDraw.Draw(img)

# Function to draw one apple
def draw_apple(x, y, color):
    # Apple body
    draw.ellipse((x, y, x + 50, y + 50), fill=color)
    # Leaf on top
    draw.rectangle((x + 20, y - 10, x + 30, y), fill="green")

# Use a loop to draw colorful apples
for i in range(10):
    # Change color slightly each time
    color = (25 * i, 80, 255 - 25 * i)
    x_position = 40 + i * 55
    draw_apple(x_position, 200, color)

# Save the image
img.save("colorful_apples.png")
print("✅ Image saved as colorful_apples.png")
