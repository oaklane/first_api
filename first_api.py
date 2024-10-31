import requests


def test_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Check response time (should be less than 2 seconds for this example)
    assert response.elapsed.total_seconds() < 2, "API response time is too slow"

    # Check the content type of the response
    assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Incorrect content type"

    # Verify response JSON content
    data = response.json()
    assert data["id"] == 1, f"Expected post ID to be 1, got {data['id']}"
    assert data["userId"] == 1, f"Expected user ID to be 1, got {data['userId']}"

    print("All tests passed!")


if __name__ == "__main__":
    test_api()
