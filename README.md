# Monster Train Leaderboard API Wrapper

This project provides a Python wrapper to access the daily challenge leaderboard of the game Monster Train. It allows users to retrieve details about challenges, leaderboards, and individual game runs.
> **Note:** The leadeboard API is neither documented nor public. The process of obtaining the session ticket through Steam API or other means is not documented here. This project assumes you have an already-generated authentication token.

## Features

- Retrieve details of daily challenges (with and without DLC).
- Access leaderboard data for specific challenges (current day or previous day only)
- Obtain detailed information on a player's run
- Game asset IDs (relics, cards, etc.) corresponding strings are stored in data/ (parsed from the modding community)

## Authentication

The Monster Train leaderboard API is unofficial and undocumented. To access the game's leaderboard endpoints, an authentication token is required. For Steam, this token is built from your Steam ID and a session authentication ticket generated by Steam/Monster Train.

### How to Obtain the Auth Token

1. **Launch Monster Train** and navigate to the daily challenge leaderboard.
2. **Monitor network traffic** using an HTTP(s) network traffic analyzer tool to capture the authentication token.
3. **Store the token** securely, as it is required for making API calls. Note that the token is time-limited (or session-limited, not sure) and must be regenerated for each session.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mt_leaderboard.git
   cd mt_leaderboard
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

1. Set up your environment:
   - Create a `.env` file in the root directory.
   - Add your authentication token:
     ```
     AUTH_TOKEN=your_auth_token_here
     ```

2. Use the API wrapper:
   ```python
   from api import MonsterTrainAPI

   api = MonsterTrainAPI(auth_token=auth_token)
   
   # Example: Get today's challenge without DLC
   vanilla_challenge = api.get_challenge(dlc=0, day=1)
   print(vanilla_challenge)
   ```

For more detailed usage examples, please refer to the `examples.py` file in the repository.

## Parsing Game Assets

The project includes parsed game asset IDs sourced from the modding community, specifically the `brandonandzeus/Trainworks2` GitHub project. These assets are used to interpret the IDs returned by the API.

## Documentation

I documented the leaderboard API is documented in a public Postman repository: [Monster Train Leaderboard API Documentation](https://documenter.getpostman.com/view/5757796/2sA3XPE3N5). Feel free to use this documentation if you wish to create your own wrapper.


## License

This project is licensed under the MIT License.

## Acknowledgements

- Game asset IDs parsed from [brandonandzeus/Trainworks2](https://github.com/brandonandzeus/Trainworks2).