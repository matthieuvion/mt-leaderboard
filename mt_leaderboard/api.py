from .client import MonsterTrainClient
from .endpoints import CHALLENGE, LEADERBOARD, GAMERUNS


class MonsterTrainAPI:
    """
    Wrapper for the Monster Train API.

    Attributes:
        client (MonsterTrainClient): The client for interacting with the Monster Train API.
    """

    def __init__(self, auth_token: str):
        """
        Initializes the MonsterTrainAPI with an authorization token.

        Args:
            auth_token (str): The authorization token.
        """
        self.client = MonsterTrainClient(auth_token)

    def get_challenge(self, challengeid: str) -> dict:
        """
        Retrieves details of a specific challenge.

        Args:
            challengeid (str): The ID of the challenge.

        Returns:
            dict: The challenge details.
        """
        url = CHALLENGE.format(challengeid=challengeid)
        return self.client.get(url)

    def get_leaderboard(
        self, challengeid: str, offset: int = 1, limit: int = 10
    ) -> dict:
        """
        Retrieves the leaderboard for a specific challenge.

        Args:
            challengeid (str): The ID of the challenge.
            offset (int, optional): The offset for pagination. Defaults to 1.
            limit (int, optional): The number of results per page. Defaults to 10.

        Returns:
            dict: The leaderboard data.
        """
        url = LEADERBOARD.format(challengeid=challengeid)
        params = {"offset": offset, "limit": limit}
        return self.client.get(url, params=params)

    def get_gameruns(self, userid: str, challengeid: str) -> dict:
        """
        Retrieves details about a specific challenge run for a specified player.

        Args:
            userid (str): The user ID (e.g., Steam ID).
            challengeid (str): The ID of the challenge.

        Returns:
            dict: The game run details.
        """
        url = GAMERUNS.format(userid=userid, challengeid=challengeid)
        return self.client.get(url)


# Example usage
if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG)

    api = MonsterTrainAPI(auth_token="your_auth_token_here")
    challenge_id = "example_challenge_id"
    user_id = "example_user_id"

    # Get challenge details
    challenge = api.get_challenge(challenge_id)
    print(challenge)

    # Get leaderboard
    leaderboard = api.get_leaderboard(challenge_id, offset=1, limit=10)
    print(leaderboard)

    # Get gameruns
    gameruns = api.get_gameruns(user_id, challenge_id)
    print(gameruns)
