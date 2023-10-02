from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver

def get_solutions_from_stackoverflow(error_name):
    print("\nSearching for solutions on StackOverflow...\n")
    BASE_URL = "https://stackoverflow.com"
    QUERY = f"/search?q={error_name}"

    try:
        response = requests.get(BASE_URL + QUERY)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Pattern to select answers summary
            pattern = re.compile('question-summary|answer-id')
            question_summary = soup.find_all('div', id=pattern)

            answers = []
            for summary in question_summary:
                # Pattern to select title, number of votes and question time
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
        print(f"An error occurred: {e}")

def show_solutions(error_name):
    solutions = get_solutions_from_stackoverflow(error_name)
    print("================================StackOveflow Solutions ========================================================\n")
    for answer in solutions:
        print("Title: ", answer['title'])
        print("Link: ", answer['link'])
        print("Number of Votes: ", answer['votes'])
        print("Date: ", answer['date'])
        print('\n')

def get_and_print_first_solution(error_name):
    driver = webdriver.Chrome()
    solutions = get_solutions_from_stackoverflow(error_name)
    if solutions:
        first_solution_url = solutions[1]['link']
        try:
            driver.get(first_solution_url)
            driver.save_screenshot("screenshot.png")
        except Exception as e:
            print(f"An error occurred while fetching the first solution: {e}")
    else:
        print("No solutions found for the error.")


if __name__ == "__main__":
    get_and_print_first_solution("ValueError")

    
    
    
