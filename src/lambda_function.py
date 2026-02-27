# Made with ❤️ by Richard | With assistance from Copilot.
# Description: AWS Lambda function to proxy Alexa events to Home Assistant using up to two tokens for authentication.
# On failure with the first token, the second is tried. Logs all errors and raises if both fail.

import os, json, logging, urllib3

# Set up logging level based on DEBUG environment variable
logger = logging.getLogger()
logger.setLevel(logging.DEBUG if os.getenv("DEBUG") == "1" else logging.INFO)

# Build the Home Assistant API URL from environment variables
URL = f"https://{os.environ['HA_URL']}{os.environ['HA_API_Path']}"

# Create a reusable HTTP connection pool
http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=2.0, read=10.0))

def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    Tries to forward the Alexa event to Home Assistant using up to two tokens.
    Returns the Home Assistant response or raises an error if both tokens fail.
    """
    logger.debug("Event: %s", json.dumps(event))
    body = json.dumps(event).encode("utf-8")
    # Collect available tokens from environment
    tokens = [t for t in [os.getenv('HA_Token_1'), os.getenv('HA_Token_2')] if t]
    last_err = None

    for idx, token in enumerate(tokens, 1):
        try:
            # Attempt to send the request with the current token
            res = http.request("POST", URL, body=body, headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            })
            if res.status < 400:
                # Success: return parsed JSON response
                return json.loads(res.data.decode("utf-8"))
            # Log error if status code indicates failure
            logger.error(f"Token {idx} failed ({res.status}): {res.data}")
            last_err = f"Status {res.status}"
        except Exception as e:
            # Log and store exception if request fails
            last_err = str(e)
            logger.error(f"Token {idx} request error: {e}")

    # Raise error if all tokens fail or none are set
    raise RuntimeError(f"HA Access Failed: {last_err if tokens else 'No tokens'}")