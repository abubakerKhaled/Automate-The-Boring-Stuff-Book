# Google Search Automation Script

This project is a simple Python script that automates the process of performing a Google search from the command line and opening the top search results in your web browser. The script uses the `requests` library to fetch the search results, `BeautifulSoup` for parsing the HTML, and `webbrowser` to open the links.

## Features

- **Automated Google Search**: Search Google directly from the command line by entering your search query as arguments.
- **Open Top Results**: Automatically open the top search results (up to 5) in your default web browser.

## Requirements

- **Python 3.x**
- **Requests**: Install with `pip install requests`
- **BeautifulSoup4**: Install with `pip install beautifulsoup4`
- **lxml**: Install with `pip install lxml`

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/google-search-automation.git
   ```

2. **Navigate to the Project Directory**:
   ```sh
   cd google-search-automation
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script**:
   ```sh
   python search.py <your search query>
   ```

2. **Example**:
   ```sh
   python search.py Python web scraping tutorial
   ```

3. The script will perform a Google search for the provided query and automatically open the top 5 search results in your default web browser.

## Script Breakdown

- **Google Search Request**: 
  - The script constructs a Google search URL using the search terms provided as command-line arguments.
  - `requests.get()` fetches the search results page.
  
- **Parsing with BeautifulSoup**:
  - The search results page is parsed using `BeautifulSoup`.
  - The script filters links that start with `"/url?q="`, which are the actual search result links.
  
- **Opening Links**:
  - The script extracts the first 5 links and opens them using the `webbrowser` module.

## Future Improvements

This project is functional but can benefit from several improvements:

1. **Error Handling**: Improve error handling for scenarios like network failures or invalid search queries.
2. **Customizable Result Count**: Allow users to specify how many top results they want to open.
3. **Headless Browser Integration**: Use Selenium or similar tools to bypass potential issues with Google blocking automated requests.
4. **Search Engine Options**: Allow the user to choose different search engines (Bing, DuckDuckGo, etc.).
5. **Logging**: Add logging to capture and save the URLs of the opened pages.

## License

This project is open-source and available under the MIT License. Feel free to contribute and suggest improvements!

---

This script is a quick and easy way to automate Google searches, but there's room for enhancements to make it more robust and versatile.