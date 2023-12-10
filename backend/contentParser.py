import requests

def fetch_website_content(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the content in bytes format
            return response.content
        else:
            print(f"Failed to fetch website content. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching website content: {e}")
        return None

# URL of the website to create a file of
url_to_fetch = 'https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500'
website_content = fetch_website_content(url_to_fetch)

if website_content:
    try:
        # Write the content to a file
        with open('website_content.html', 'wb') as file:
            file.write(website_content)
        print("Website content written to 'website_content.html'")
    except Exception as e: # Error handling
        print(f"Error writing content to file: {e}")
else:
    print("No content retrieved from the website.")
