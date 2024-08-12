import requests, sys, webbrowser, bs4

print("Searching...")
# Perform a Google search
res = requests.get("https://www.google.com/search?q=" + " ".join(sys.argv[1:]))

res.raise_for_status()

src = res.content

# Parse the Google search result page
soup = bs4.BeautifulSoup(src, "lxml")


# Filter the Google search result links within <a> tags that start with "/url?q="
linkElems = soup.select('a[href^="/url?q="]')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    link = linkElems[i].get("href")
    if link and link.startswith("/url?q="):
        # Extract the actual URL, ignoring Google-specific parameters
        urlToOpen = link.split("/url?q=")[1].split("&")[0]
        print("Opening " + urlToOpen)
        webbrowser.open(urlToOpen)
