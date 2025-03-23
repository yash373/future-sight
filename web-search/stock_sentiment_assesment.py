from searchclient import get_search_results
from llmclient import get_response

def get_sentiment(stock_name: str) -> str:
    # Questions that will be extracted for using searchclient
    search_questions = [
        f"What is the current public sentiment about {stock_name} stock?",
        # f"How do investors feel about {stock_name} stock performance?",
        # f"Is {stock_name} stock considered overvalued or undervalued by the market?",
        # f"What recent news is influencing investor sentiment towards {stock_name} stock?",
        # f"What are experts saying about the future prospects of {stock_name} stock?"
    ]

    # Getting search results for questions in search questions
    print("Getting search results")
    search_results = [
        get_search_results(search_questions[0])[:1000],
        # get_search_results(search_questions[1])[:1000],
        # get_search_results(search_questions[2])[:1000],
        # get_search_results(search_questions[3])[:1000],
        # get_search_results(search_questions[4])[:1000]
    ]

    # Printing the search results [Testing]
    print("Search Results:")
    for i, result in enumerate(search_results):
        print(f"Question: {search_questions[i]}")
        print("Answers:")
        for answer in result:
            print(answer)
        print("")

    # Creating the query that will be passed to the llm for processing

    # Combining the search results with their reqpective search quesries
    temp = ""
    for index, question in enumerate(search_questions):
        temp += f"Question: {question}\nAnswer: {search_results[index]}\n"
    
    # Writing the final query that will be pushed to the llm
    query = f"""
    You are a financial analyst who is analyzing the sentiment of investors towards a stock. The stock is {stock_name}. You made the following searches and you got the following search reults. Analyze the sentiment and rate it form 0 to 100 [ANSWER IN NUMBERS].\n
    {temp}
    """

    # Printing the query [Testing]
    print(f"Query:\n{query}")

    # Getting the response from llm
    print("Prompting llm")
    return get_response(query)


print(get_sentiment("RELIANCE"))