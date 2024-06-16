import logging

import httpx
from exceptions import APIError


class MonsterTrainClient:
    """
    Client for interacting with the Monster Train API.

    Attributes:
        auth_token (str): The authorization token for authenticating API requests.
        client (httpx.Client): The HTTP client for sending requests.
        logger (logging.Logger): The logger for logging messages.
    """

    def __init__(self, auth_token: str):
        """
        Initializes the MonsterTrainClient with an authorization token.

        Args:
            auth_token (str): The authorization token.
        """
        self.auth_token = auth_token
        self.client = httpx.Client(
            headers={
                "Authorization": f"Bearer {self.auth_token}",
                "User-Agent": "UnityPlayer/2019.4.4f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
                "Accept-Encoding": "identity",
                "ShinyShoe-Build-Number": "12923",
                "X-Unity-Version": "2019.4.4f1",
            }
        )
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def _handle_response(self, response: httpx.Response) -> dict:
        """
        Handles the HTTP response, checking for errors.

        Args:
            response (httpx.Response): The HTTP response.

        Returns:
            dict: The JSON response.

        Raises:
            APIError: If the response status code is not 200.
        """
        if response.status_code != 200:
            self.logger.error(
                f"API request failed with status code {response.status_code}: {response.text}"
            )
            raise APIError(
                f"API request failed with status code {response.status_code}: {response.text}"
            )
        self.logger.debug(f"API request succeeded with response: {response.text}")
        return response.json()

    def get(self, url: str, params: dict = None) -> dict:
        """
        Sends a GET request to the specified URL with optional parameters.

        Args:
            url (str): The URL to send the GET request to.
            params (dict, optional): The query parameters for the GET request.

        Returns:
            dict: The JSON response.
        """
        self.logger.debug(f"Sending GET request to URL: {url} with params: {params}")
        response = self.client.get(url, params=params)
        return self._handle_response(response)
