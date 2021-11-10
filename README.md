# `About`
A CLI Password Manager that can save your passwords securely in images using [Steganography](https://en.wikipedia.org/wiki/Steganography). The program can also generate strong passwords for your use

# `Installation`
1. Download or clone the [repository](https://github.com/advaitjadhav/Password-manager).
2. Install the dependencies by running the command below.
> pip install -r requirements.txt
3. Now run the `setup.py` file.
> python setup.py install
4. Once, the setup is completed you will be able to run `pypassword` command.
### Preview
```
$ pypassword 
Usage: pypassword [OPTIONS] COMMAND [ARGS]...

  A CLI Password Manager that can save your passwords securely in images using
  Steganography. The program can also generate strong passwords for your use.

Options:
  --help  Show this message and exit.

Commands:
  decrypt            Decrypts encoded text from image.
  encrypt            Encrypts password into image.
  generate-password  Generates a strong password!
```

# `How to use`
### Encryption
```
$ pypassword encrypt
Enter your password: nopassword
Enter the path of the image you want to hide your password(with extension): Macbook.png
Enter the path to save encoded image with extension(Leave blank to save in current working directory): encoded_macbook.png

Your password(nopassword) has been successfully encoded in the image(Macbook.png)
Encoded image has been saved associated with the entered name(encoded_macbook.png)!
```
- `Macbook.png`
![Macbook](https://user-images.githubusercontent.com/76993204/141080972-5b410eea-c7e9-4ff3-b794-e56d6f12f723.png)

- `encoded_macbook.png`
![encoded_macbook](https://user-images.githubusercontent.com/76993204/141080946-736ac3db-2805-4797-a1a4-d436335850bf.png)

### Decryption
```
$ pypassword decrypt
Enter the path of the image your password is hidden in(with extension): encoded_macbook.png
Decrypted password-> nopassword
```

# `Depends On`
- click==8.0.1
- tweepy==4.3.0
- setuptools==56.0.0
- Pillow==8.4.0
- PyInquirer==1.0.3
- rich==10.13.0

# `Made with`
- Python[^3.8]
- [Replit](https://replit.com/)(Development Environment)

# `Bug Tracking`
If any bugs are found make sure to create a new [issue](https://github.com/advaitjadhav/Password-manager/issues)