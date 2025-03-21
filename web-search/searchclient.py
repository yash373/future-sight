import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS


def get_body_texts(query: str, max_links: int = 20):
    """
    Returns the text from the body of the first max_links search results for a given query.

    Parameters:
        query (str): The search query.
        max_links (int): The maximum number of links to process.

    Returns:
        list of str: A list containing the text from the body of each page.
    """
    texts = []

    # Use the DDGS class to perform the search
    with DDGS() as ddgs:
        # The text method returns a generator of search result dictionaries.
        results = list(ddgs.text(query, max_results=max_links))

    if not results:
        print("No results found for the query.")
        return texts

    # Process each search result link
    for result in results:
        # The URL may be stored under 'href' or 'url'
        url = result.get("href") or result.get("url")
        if not url:
            continue

        try:
            # Fetch the webpage
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract text from the <body> tag, if it exists
            body = soup.body
            if body:
                text = body.get_text(separator="\n", strip=True)
                texts.append(text)
            else:
                texts.append("")
        except Exception as e:
            print(f"Error processing {url}: {e}")
            texts.append("")

    return texts


# Example usage:
# if __name__ == "__main__":
#     query = "Python programming tutorials"
#     body_texts = get_body_texts(query)

#     for idx, text in enumerate(body_texts):
#         print(f"--- Link {idx + 1} Content (first 200 characters) ---")
#         print(text[:200])
#         print()
