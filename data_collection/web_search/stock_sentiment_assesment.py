from .searchclient import get_search_results
from .llmclient import get_response


def get_sentiment(search_question: str, stock_name: str) -> str:
    # Fetching the search results
    search_results = get_search_results(f"{search_question}", num_results=5)

    # Printing the search results [Testing]
    print("Search Results:")
    print(search_results)

    # Getting Summary
    print("Summarizing Results")
    summary = get_response(
        f"Summarize and make sure to add all important details regarding {stock_name} from the search results.\n{search_results}"
    )
    print(summary)

    # Creating the query that will be passed to the llm for processing

    # Combining the search results with their reqpective search quesries
    temp = f"Question: {f"{search_question}"}\nAnswer: {summary}\n"

    # Writing the final query that will be pushed to the llm
    query = f"""
    You are provided with some search information and the results, your task is to analyse the sentiment of the search results and RATE IT FROM 0 to 100 [50 -> Neutral, 0 -> Negative, 100 -> Positive] solely based off the given data and answer just using a number only and nothing else\n
    {temp}
    """

    # Printing the query [Testing]
    print(f"Query:\n{query}")

    # Getting the response from llm
    print("Prompting llm")
    return int(get_response(query))


# stock_name = "TATA CONSULTANCY SERVICES"
# company_performance = get_sentiment(
#     stock_name=stock_name,
#     search_question=f"How does the {stock_name}'s latest earnings report impact its stock sentiment?",
# )
# print(company_performance)
