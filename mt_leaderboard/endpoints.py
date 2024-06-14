BASE_URL = "https://ocffhwpt3b.execute-api.us-west-2.amazonaws.com/production/api/v1/"

# Endpoints
CHALLENGE = BASE_URL + "challenge/{challengeid}"
LEADERBOARD = BASE_URL + "leaderboard/daily/{challengeid}"
GAMERUNS = BASE_URL + "gameruns/{userid}/{challengeid}"
