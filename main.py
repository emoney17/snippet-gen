from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def main():

    # Colors
    colorWhite = (225, 225, 225)
    colorRed   = (225, 0, 0) 
    colorBlue  = (0, 0, 225)
    colorGreen = (0, 225, 0)

    # Open image
    img = Image.open("./imgs/black.jpg")

    # Call draw method to add graphics to image
    snippet = ImageDraw.Draw(img)

    # Custom font and size
    myFont = ImageFont.truetype("./font/CaskaydiaCove-Regular.ttf", 32)

    myString = "#include <iostream>\n\nint main() {\n    std::cout << \"Hello world\" << std::endl;\n    return 0;\n}\n"

    # Coordinates
    x = 10
    y = 0

    # Input string
    mySplit = myString.split('\n')

    # Draw each line
    for line in mySplit:
        snippet.text((x, y), line, font=myFont, fill =(colorWhite))

        # Move down 50 pix
        y += 50

    # Show the edit
    img.show()

if __name__ == "__main__":
    main()
