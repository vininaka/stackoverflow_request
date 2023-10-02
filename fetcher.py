from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver

def get_solutions_from_stackoverflow(error_name):
    BASE_URL = "https://stackoverflow.com"
    QUERY = f"/search?q={error_name}"

    try:
        response = requests.get(BASE_URL + QUERY)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        soup = BeautifulSoup(response.text, "html.parser")

        # Pattern to select question summaries and answers
        pattern = re.compile('question-summary|answer-id')
        question_summary = soup.find_all('div', id=pattern)

        answers = []
        for summary in question_summary:
            # Pattern to select title, number of votes, and question time
            pattern_title = re.compile('s-link|answer-hyperlink')
            title = summary.find("a", class_=pattern_title)
            votes = summary.find("span", class_='s-post-summary--stats-item-number')
            time = summary.find("span", class_='relativetime')

            answers.append({
                'title': title.get_text(),
                'link': BASE_URL + title['href'],
                'votes': votes.text,
                'date': time.text
            })
        return answers
    except Exception as e:
        print(f"An error occurred while fetching solutions: {e}")
        return []

def show_solutions(error_name):
    print("\nSearching for solutions on StackOverflow...\n")
    solutions = get_solutions_from_stackoverflow(error_name)
    if solutions:
        print("================================ StackOverflow Solutions ================================================\n")
        for answer in solutions:
            print("Title: ", answer['title'])
            print("Link: ", answer['link'])
            print("Number of Votes: ", answer['votes'])
            print("Date: ", answer['date'])
            print('\n')
    else:
        print("No solutions found for the error.")

def get_and_print_first_solution(error_name):
    print("\nFetching and saving a screenshot of the first solution...\n")
    solutions = get_solutions_from_stackoverflow(error_name)
    if solutions:
        first_solution_url = solutions[0]['link']
        try:
            driver = webdriver.Chrome()
            driver.get(first_solution_url)
            driver.save_screenshot("screenshot.png")
            driver.quit()  # Close the WebDriver after use
        except Exception as e:
            print(f"An error occurred while fetching the first solution: {e}")
    else:
        print("No solutions found for the error.")

if __name__ == "__main__":
    error_name = "ValueError"  # Replace with your desired error name
    show_solutions(error_name)
    get_and_print_first_solution(error_name)