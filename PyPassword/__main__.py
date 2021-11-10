import random
import string
import array
import os

try:
    from . import steganography
    import click
    from rich.console import Console
    from rich.markdown import Markdown
    from PyInquirer import prompt
    from examples import custom_style_1

except ModuleNotFoundError:
    with open("requirements.txt", 'r') as f:
        print(f"""
[ERROR] Unmet Dependencies!
# Depends On
{f.read()}

Installing Dependencies...
    """)
    os.system("pip install -r requirements.txt")

    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

    exit(print("\nDependencies installed! Please re-run the application."))

CHARACTERS = list(string.ascii_lowercase + string.ascii_uppercase)
DIGITS = list(string.digits)
SYMBOLS = ['!', '@', '#', '$', '^', '*', '_']

console = Console()
temp_pass = ''


@click.group()
def main():
    """A CLI Password Manager that can save your passwords securely in images using Steganography. The program can also generate strong passwords for your use."""
    pass


@main.command()
@click.option(
    '--characters',
    '-c',
    prompt="Number of characters(Leave blank for default). Default-->",
    default=6,
    help='Number of characters in your password.')
@click.option('--digits',
              '-d',
              prompt="Number of digits(Leave blank for default). Default-->",
              default=4,
              help='Number of digits in your password.')
@click.option('--symbols',
              '-s',
              prompt="Number of symbols(Leave blank for default). Default-->",
              default=1,
              help='Number of symbols in your password.')
def generate_password(characters, digits, symbols):
    """Generates a strong password!"""
    global temp_pass

    for char in range(0, characters):
        ch = CHARACTERS[random.randint(0, len(CHARACTERS) - 1)]
        temp_pass += ch
    for dig in range(0, digits):
        dg = DIGITS[random.randint(0, len(DIGITS) - 1)]
        temp_pass += dg
    for sym in range(0, symbols):
        sy = SYMBOLS[random.randint(0, len(SYMBOLS) - 1)]
        temp_pass += sy

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    final_password = ''

    for x in temp_pass_list:
        final_password += x

    md = Markdown(f"""

- Password--> {final_password}
        

> We highly recommend to save passwords if you are looking forward to use them. Saved passwords are securely hidden into images using [Steganography](https://en.wikipedia.org/wiki/Steganography).

    """)

    console.print(md)

    questions = [{
        'type': 'confirm',
        'name': 'confirm',
        'message': 'Would you like to save this password?',
        'deafault': True
    }]

    answers = prompt(questions, style=custom_style_1)

    if answers["confirm"] == True:
        path_q = [{
            'type':'input',
            'name':'img_path',
            'message':'Enter the path of the image you want to hide your password(with extension):'
        },
        {
            'type':'input',
            'name':'img_out',
            'message':'Enter the name for encoded image(with extension):'
        }]

        path_a = prompt(path_q, style=custom_style_1)

        encrypt(final_password, path_a["img_path"], path_a["img_out"])


@main.command()
@click.option("--password",
              "-p",
              prompt="Enter your password",
              help="Password to be encoded in image.")
@click.option(
    "--image",
    "-i",
    prompt=
    "Enter the path of the image you want to hide your password(with extension)",
    help="Name of the image password will be encoded in!")
@click.option(
    "--out",
    "-o",
    prompt=
    "Enter a name for encoded image with extension(Encoded image will be saved in working directory.)",
    help="Name of the encoded image.")
def encrypt(password, image, out):
    """Encrypts password into image."""
    try:
        steganography.encode(image, password, out)
    except FileNotFoundError:
        print(f"[ERROR] No file named {image} found!")
        exit()

    console.print(
        f"\nYour password({password}) has been successfully encoded in the image({image})\nEncoded image has been saved associated with the entered name({out})!"
    )


@main.command()
@click.option(
    "--image",
    "-i",
    prompt=
    "Enter the path of the image your password is hidden in(with extension)",
    help="Name of the image password is saved in!")
def decrypt(image):
    """Decrypts encoded text from image."""
    try:
        console.print(
            f"Decrypted password-> [bold underline magenta]{steganography.decode(image)}[/]"
        )
    except FileNotFoundError:
        print(f"[ERROR] No file named {image} found!")
        exit()


if __name__ == "__main__":
    main()
