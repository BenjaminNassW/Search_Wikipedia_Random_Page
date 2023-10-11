import wikipedia


def fetch_random_wikipedia_article():
    try:
        # Set the user agent for the Wikipedia library
        wikipedia.set_lang("en")

        # Fetch a random Wikipedia article
        random_article_title = wikipedia.random()
        return random_article_title
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    try:
        while True:
            random_article_title = fetch_random_wikipedia_article()
            if random_article_title:
                print("Random Wikipedia Article:", random_article_title)

                # Ask the user if they want to read the article
                user_choice = input("Do you want to read this article? (yes/no): ").strip().lower()

                if user_choice == "yes":
                    # Fetch and print the article content
                    article_content = wikipedia.page(random_article_title).content
                    print(article_content)
                else:
                    print("Okay, let's find another random article.")

                # Ask if the user wants to continue
                continue_choice = input("Do you want to fetch another random article? (yes/no): ").strip().lower()

                if continue_choice != "yes":
                    print("Goodbye!")
                    break
    except KeyboardInterrupt:
        print("Program terminated by the user.")

if __name__ == "__main__":
    main()
