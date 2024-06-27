import string
import random

# In-memory database to store short and original URLs
url_database = {}

# Generate a random short URL path
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

# Shorten a URL
def shorten_url(original_url):
    if original_url in url_database:
        # If the URL is already shortened, return the existing short URL
        return url_database[original_url]
    else:
        # Otherwise, generate a new short URL
        short_url = generate_short_url()
        url_database[original_url] = short_url
        url_database[short_url] = original_url
        return short_url

# Retrieve the original URL from a short URL
def retrieve_url(short_url):
    return url_database.get(short_url, None)

# Main program loop
def main():
    while True:
        print("\nURL Shortener")
        print("1. Shorten a URL")
        print("2. Retrieve a URL")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            original_url = input("Enter the URL to shorten: ")
            short_url = shorten_url(original_url)
            print(f"Short URL is: {short_url}")
        elif choice == '2':
            short_url = input("Enter the short URL to retrieve: ")
            original_url = retrieve_url(short_url)
            if original_url:
                print(f"Original URL is: {original_url}")
            else:
                print("Short URL not found.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
