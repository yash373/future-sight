import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def get_search_results(query, num_results=20):
    """
    Searches DuckDuckGo for the given query, fetches the first n results,
    and extracts the text content from the body of each webpage.
    
    Args:
        query (str): The search query to use
        num_results (int): Number of search results to process (default: 20)
        
    Returns:
        list: List of dictionaries containing URL and extracted text for each result
    """
    # Initialize results list
    results = []
    
    # Initialize DuckDuckGo search
    ddgs = DDGS()
    
    try:
        # Perform the search
        search_results = list(ddgs.text(query, max_results=num_results))
        
        # Process each search result
        for i, result in enumerate(search_results):
            if i >= num_results:
                break
                
            url = result.get('href')
            if not url:
                continue
                
            try:
                # Fetch the webpage content
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Extract text from the body
                if soup.body:
                    # Get text and clean it up
                    text = soup.body.get_text(separator=' ', strip=True)
                    # Remove extra whitespace
                    text = ' '.join(text.split())
                    
                    results.append({
                        'url': url,
                        'title': result.get('title', ''),
                        'text': text[:1000]
                    })
                else:
                    results.append({
                        'url': url,
                        'title': result.get('title', ''),
                        'text': 'No body content found'
                    })
                
                print(f"Processing result {i+1}: {url}")
            except Exception as e:
                results.append({
                    'url': url,
                    'title': result.get('title', ''),
                    'text': f'Error fetching content: {str(e)}'
                })
    
    except Exception as e:
        return {'error': f'Search failed: {str(e)}'}
    
    return results

# Example usage
# if __name__ == "__main__":
#     search_query = "python wikipedia"
#     content = get_search_results(search_query)
    
#     # Print the results
#     for i, item in enumerate(content):
#         print(f"\n--- Result {i+1} ---")
#         print(f"URL: {item['url']}")
#         print(f"Title: {item['title']}")
#         print(f"Text preview: {item['text'][:150]}...")