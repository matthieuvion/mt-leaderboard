BASE_URL = "https://ocffhwpt3b.execute-api.us-west-2.amazonaws.com/production/api/v1/"

# Endpoints
CHALLENGE = BASE_URL + "challenge"
LEADERBOARD = BASE_URL + "leaderboard/daily/{challenge_id}"
GAMERUNS = BASE_URL + "gameruns/{user_id}/{run_id}"
