import httpx
import asyncio


async def request_with_retries(
        method: str,
        url: str,
        data=None,
        query_params=None,
        max_retries=3,
        retry_delay=2
):
    """Helper function to perform HTTP requests with retries."""
    attempt = 0
    while attempt < max_retries:
        try:
            async with httpx.AsyncClient() as client:
                # Choose the correct HTTP method based on the method parameter
                if method.lower() == "post":
                    response = await client.post(url, json=data)
                elif method.lower() == "get":
                    response = await client.get(url, params=query_params)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")

                # Check the response status code
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Failed to make a request, status code: {response.status_code}, {response.json()}")
                    raise Exception("Failed to join node")

        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            print(f"Request error on attempt {attempt + 1}: {e}")

        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {e}")

        attempt += 1
        print(f"Retrying... ({attempt}/{max_retries})")
        await asyncio.sleep(retry_delay)  # Wait before retrying

    print(f"All {max_retries} attempts failed. Could not to make a request.")
    raise Exception(f"All {max_retries} attempts failed. Could not join node.")


async def post(url: str, data=None, max_retries=3, retry_delay=2):
    """POST request function with retry logic."""
    return await request_with_retries("post", url, data, max_retries, retry_delay)


async def get(url: str, query_params=None, max_retries=3, retry_delay=2):
    """GET request function with retry logic."""
    return await request_with_retries("get", url, query_params, max_retries=max_retries, retry_delay=retry_delay)
