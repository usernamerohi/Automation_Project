#import cisco
import requests
import json


def search_privacy_policy(company=None):
    api_key = '8dafc4155a8eed609c5a7ce062b4ec79a63d6140e07859347bd91c3d0c182f4f'
    search_engine = 'google'
    search_query = f'{company} privacy policy'
    num_results = 10  # Number of results to retrieve

    # SerpAPI endpoint URL
    url = f'https://serpapi.com/search.json?q={search_query}&engine={search_engine}&num={num_results}&api_key={api_key}'

    try:
        # Send GET request to SerpAPI
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse JSON response
        data = response.json()

        # Extract search results
        search_results = data.get('organic_results', [])

        # Extract URLs from search results
        urls = [result.get('link') for result in search_results]

        return urls

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    except json.JSONDecodeError as json_err:
        print(f"JSON Decode Error: {json_err}")

    return []


# Example usage:
if __name__ == "__main__":
    company_name = "https://www.facebook.com/"
    privacy_policy_urls = search_privacy_policy()
    print("privacy policy urls: ", privacy_policy_urls)

    if privacy_policy_urls:
        print(f"Found privacy policy URLs for '{company_name}':")
        for idx, url in enumerate(privacy_policy_urls, start=1):
            print(f"{idx}. {url}")
    else:
        print(f"No privacy policy URLs found for '{company_name}'")