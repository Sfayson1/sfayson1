from PIL import Image, ImageDraw, ImageFont


def generate_section_header(number, title, filename):
    width = 1200
    height = 160

    background_color = "#08233F"
    navy = "#163B67"
    coral = "#F47A61"
    turquoise = "#27B3B1"
    gradient_start = (244, 122, 97)
    gradient_middle = (245, 158, 66)
    gradient_end = (39, 179, 177)

    image = Image.new("RGB", (width, height), background_color)

    draw = ImageDraw.Draw(image)

    midpoint = width // 2

    for x in range(midpoint):
        ratio = x / midpoint
        red = int(gradient_start[0] + (gradient_middle[0] - gradient_start[0] * ratio))
        green = int(
            gradient_start[1] + (gradient_middle[1] - gradient_start[1] * ratio)
        )
        blue = int(gradient_start[2] + (gradient_middle[2] - gradient_start[2] * ratio))
        color = (red, green, blue)

        draw.line((x, height - 4, x, height), fill=color)

    for x in range(midpoint, width):
        ratio = (x - midpoint) / midpoint
        red = int(gradient_middle[0] + (gradient_end[0] - gradient_middle[0]) * ratio)
        green = int(gradient_middle[1] + (gradient_end[1] - gradient_middle[1]) * ratio)
        blue = int(gradient_middle[2] + (gradient_end[2] - gradient_middle[2]) * ratio)
        color = (red, green, blue)
        draw.line((x, height - 4, x, height), fill=color)

    draw.rectangle((0, 0, 12, height), fill=coral)

    draw.rectangle((170, 55, 172, 105), fill=turquoise)

    number_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 42)

    title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 38)

    draw.text((50, 52), number, font=number_font, fill=coral)

    draw.text((190, 55), title, font=title_font, fill="white")

    sunset_box = (1010, 35, 1100, 125)

    draw.ellipse(sunset_box, fill=coral)

    for y in range(82, 120, 8):
        draw.rectangle((1010, y, 1100, y + 3), fill=background_color)

    image.save(filename)


generate_section_header(
    "01 //", "ENGINEER PROFILE", "assets/section-01-engineer-profile.png"
)
generate_section_header(
    "02 //", "FEATURED BUILD", "assets/section-02-featured-build.png"
)
generate_section_header(
    "03 //", "ENGINEERING TOOLKIT", "assets/section-03-engineering-toolkit.png"
)
generate_section_header(
    "04 //", "CURRENTLY LEARNING", "assets/section-04-currently-learning.png"
)
generate_section_header("05 //", "EDUCATION", "assets/section-05-education.png")


def generate_button(label, filename, background_color):
    width = 220
    height = 60

    image = Image.new(
        "RGB",
        (width, height),
        background_color
    )

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(
        "/System/Library/Fonts/Helvetica.ttc",
        22
    )

    # Create a transparent canvas so the corners can actually be rounded
    button = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0)
    )

    button_draw = ImageDraw.Draw(button)

    button_draw.rounded_rectangle(
        (0, 0, width - 1, height - 1),
        radius=16,
        fill=background_color
    )

    # Measure the text so it can be centered
    text_box = button_draw.textbbox(
        (0, 0),
        label,
        font=font
    )

    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2 - 2

    button_draw.text(
        (x, y),
        label,
        font=font,
        fill="white"
    )

    button.save(filename)


generate_button(
    "PORTFOLIO",
    "assets/button-portfolio.png",
    "#F47A61"
)

generate_button(
    "LINKEDIN",
    "assets/button-linkedin.png",
    "#27B3B1"
)

generate_button(
    "EMAIL",
    "assets/button-email.png",
    "#163B67"
)

generate_button(
    "LIVE DEMO",
    "assets/button-live-demo.png",
    "#F47A61"
)

generate_button(
    "REPOSITORY",
    "assets/button-repository.png",
    "#27B3B1"
)
