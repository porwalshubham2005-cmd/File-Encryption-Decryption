def caesar_encrypt(text, shift):
    result = ""

    for char in text:

        if char.isupper():
            result += chr(
                (ord(char) - ord('A') + shift) % 26
                + ord('A')
            )

        elif char.islower():
            result += chr(
                (ord(char) - ord('a') + shift) % 26
                + ord('a')
            )

        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def encrypt_file(file_path, shift):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        encrypted_content = caesar_encrypt(content, shift)

        output_file = file_path.rsplit(".", 1)[0] + "_encrypted.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(encrypted_content)

        print("\nFile encrypted successfully!")
        print("Encrypted file:", output_file)

    except FileNotFoundError:
        print("\nError: File not found.")

    except Exception as error:
        print("\nError:", error)


def decrypt_file(file_path, shift):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        decrypted_content = caesar_decrypt(content, shift)

        output_file = file_path.rsplit(".", 1)[0] + "_decrypted.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(decrypted_content)

        print("\nFile decrypted successfully!")
        print("Decrypted file:", output_file)

    except FileNotFoundError:
        print("\nError: File not found.")

    except Exception as error:
        print("\nError:", error)


def main():

    print("=" * 45)
    print("   BASIC FILE ENCRYPTION/DECRYPTION")
    print("=" * 45)

    print("\n1. Encrypt File")
    print("2. Decrypt File")

    choice = input("\nEnter your choice (1/2): ")

    file_path = input("Enter file path: ")

    try:
        shift = int(input("Enter encryption key (1-25): "))

        if shift < 1 or shift > 25:
            print("Please enter a key between 1 and 25.")
            return

    except ValueError:
        print("Invalid key. Please enter a number.")
        return

    if choice == "1":

        encrypt_file(file_path, shift)

    elif choice == "2":

        decrypt_file(file_path, shift)

    else:

        print("Invalid choice.")


if __name__ == "__main__":
    main()