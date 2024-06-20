from mt_leaderboard.client import MonsterTrainClient
from mt_leaderboard.endpoints import CHALLENGE, GAMERUNS, LEADERBOARD
from mt_leaderboard.models.challenge import Challenge
from mt_leaderboard.models.gamerun import Gamerun
from mt_leaderboard.models.leaderboard import Leaderboard


class MonsterTrainAPI:
    """
    Wrapper for the Monster Train API.

        Attributes:
            client (MonsterTrainClient): The client for interacting with the Monster Train API.
    """

    def __init__(self, auth_token: str):
        """
        Initializes the MonsterTrainsAPI with an authorization token

        Args:
            auth_token (str): The authorization token.
        """
        self.client = MonsterTrainClient(auth_token)

    def get_challenge(self, dlc: int = 1, day: int = 1) -> Challenge:
        """
        Retrieves details of today or last day challenge

        Args:
            dlc (int) : 0 for no DLC challenge, 1 for paid extension (DLC) enabled.
            day (int) : 0 or 1 for today's challenge, -1 for previous day (older challenges not accessible)

        Returns:
            dict: The challenge details.
        """
        url = CHALLENGE.format(dlc)
        params = {"dlc": dlc, "offsetsequence": day}
        response = self.client.get(url, params=params)
        return Challenge(**response)

    def get_leaderboard(
        self, challenge_id: str, offset: int = 1, limit: int = 10
    ) -> Leaderboard:
        """
        Retrieves the leaderboard (a specific page) for a given challenge

        Args:
            challenge_id (str): The ID of the challenge.
            offset (int): Pagination. Start is 1
            limit (int): The number of results per page. Defaults API behavior to 10, max is 25 (even if limit set to 50)

        Returns:
            dict: The leaderboard data.
        """
        url = LEADERBOARD.format(challenge_id=challenge_id)
        params = {"offset": offset, "limit": limit}
        response = self.client.get(url, params=params)
        return Leaderboard(**response)

    def get_gamerun(self, user_id: str, run_id: str) -> Gamerun:
        """
        Retrieves details about a specific challenge run for a specified player.

        Args:
            user_id (str): The user ID (e.g., Steam ID).
            run_id (str): The ID of the run (accessible through challenge leaderboard response).

        Returns:
            dict: The game run details.
        """
        url = GAMERUNS.format(user_id=user_id, run_id=run_id)
        response = self.client.get(url)
        return Gamerun(**response)
