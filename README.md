## How It Works

1. The script sends an HTTP request to the Globo homepage.
2. It parses the HTML content using BeautifulSoup.
3. It identifies headlines based on specific CSS classes (`post__title` and `post-multicontent__link--title__text`).
4. The extracted headlines are stored in a dictionary with their corresponding URLs.
