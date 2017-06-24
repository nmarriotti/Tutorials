from passlib.hash import sha256_crypt

def main():
    password = sha256_crypt.encrypt("password")
    password2 = sha256_crypt.encrypt("password")

    print('Encrypted password: {}'.format(password))
    print('Encrypted password2: {}'.format(password2))

    print(sha256_crypt.verify("password", password))

if __name__ == "__main__":
    main()