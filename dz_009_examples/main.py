from prime_generator import generate_primes
from url_shortener import URLShortener


def main():
    url_shortener = URLShortener()

    while True:
        choice = input(
            "1. Shorten URL\n2. Get Long URL\n3. Exit\nChoose an option: ")
        if choice == '1':
            long_url = input("Enter the long URL: ")
            short_url = url_shortener.shorten_url(long_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            long_url = url_shortener.get_long_url(short_url)
            print(f"Long URL: {long_url}")
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()


def main():
    limit = int(input("Enter the limit for prime numbers: "))
    primes = generate_primes(limit)
    print(f"Prime numbers up to {limit}: {primes}")


if __name__ == "__main__":
    main()
