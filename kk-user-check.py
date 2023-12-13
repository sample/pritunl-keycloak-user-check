import requests
from pritunl import logger

# Constants for Keycloak configuration
KEYCLOAK_URL = 'https://<url>' # Replace with your actual keycloak url
REALM = '<you realm>' # Replace with your actual realm
CLIENT_ID = '<pritunl client for user checks>' # Replace with your actual client name
CLIENT_SECRET = '<token>'  # Replace with your actual client secret
DEBUG = False  # Set to True to enable debug logging
SEARCH_BY_EMAIL = False  # Set to True to search by email, False to search by username
CHECK_EMAIL_VERIFICATION = True  # Set to True to check if the email is verified

# Function to log debug information
def debug_log(message):
    if DEBUG:
        logger.debug(message)

# Function to obtain a token from Keycloak
def get_keycloak_token():
    # Payload for the token request
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    try:
        # Making a POST request to get the token
        token_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"
        debug_log(f"Requesting Keycloak token: URL={token_url}, Payload={payload}")
        response = requests.post(token_url, data=payload)

        # Logging response body for debugging
        debug_log(f"Response Body: {response.text}")

        response.raise_for_status()  # Raises an exception for HTTP errors
        token = response.json().get("access_token")
        return token
    except requests.RequestException as e:
        # Logging in case of a request failure
        logger.error("Error in obtaining Keycloak token", "keycloak_token", error=str(e))
        return None

# Function to determine if access should be denied based on user's status in Keycloak
def should_deny_access(keycloak_token, user_identifier):
    # Determine the search parameter based on the setting
    search_param = 'email' if SEARCH_BY_EMAIL else 'username'

    # Headers with the authorization token
    headers = {'Authorization': f'Bearer {keycloak_token}'}
    user_url = f"{KEYCLOAK_URL}/admin/realms/{REALM}/users?{search_param}={user_identifier}"
    try:
        # Making a GET request to check the user's status
        debug_log(f"Checking user status: URL={user_url}, Headers={headers}")
        response = requests.get(user_url, headers=headers)

        # Logging response body for debugging
        debug_log(f"Response Body: {response.text}")

        response.raise_for_status()  # Raises an exception for HTTP errors

        user_info = response.json()
        if not user_info:
            return 'User not found in Keycloak'

        user = user_info[0]
        if user.get('enabled') == False:
            return 'User is blocked in Keycloak'

        if CHECK_EMAIL_VERIFICATION and user.get('emailVerified') == False:
            return 'User email is not verified in Keycloak'

        return None  # User is allowed
    except requests.RequestException as e:
        logger.error("Error in requesting user information", "user_check", error=str(e))
        return 'Error checking user status'
    except ValueError as e:
        # Error parsing JSON
        logger.error("Error parsing JSON from Keycloak response", "json_parse_error", error=str(e))
        return 'Error parsing server response'

# user_connect hook
def user_connect(user_name, **kwargs):
    # Obtaining the Keycloak token
    keycloak_token = get_keycloak_token()
    if not keycloak_token:
        # Return False if unable to obtain a Keycloak token
        return False, 'Unable to obtain Keycloak token'

    # Determine if access should be denied
    status = should_deny_access(keycloak_token, user_name)
    if status:
        # Return False if the user should be denied access
        logger.info(f"Access denied for user \"{user_name}\". Reason: {status}")
        return False, status

    # Return True, None to allow connection if the user is allowed
    return True, None
