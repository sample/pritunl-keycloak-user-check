# pritunl-keycloak-user-check

## Description
The `pritunl-keycloak-user-check` is a plugin for Pritunl that checks if a user is available in Keycloak. It enhances the security and flexibility of VPN access management by leveraging Keycloak's authentication system. This repository also includes documentation on integrating Pritunl SSO with Keycloak.

## What the Script Does
The script acts as a middleware between Pritunl and Keycloak, performing real-time user status checks during VPN connection attempts. It ensures that:
- Only users with valid credentials in Keycloak are allowed to access the Pritunl VPN.
- Users blocked in Keycloak or with unverified email (optional check) are denied VPN access.

## Configuration Parameters
Before deploying the script, you need to adjust several parameters to match your Keycloak and Pritunl setup:

- `KEYCLOAK_URL`: The URL of your Keycloak instance.
- `REALM`: The realm in Keycloak where your users are managed.
- `CLIENT_ID`: The client ID for the Keycloak client used for authentication.
- `CLIENT_SECRET`: The client secret associated with your Keycloak client.
- `DEBUG`: Set to `True` for detailed logging, useful for debugging.
- `SEARCH_BY_EMAIL`: Set to `True` to search users by email, `False` to search by username.
- `CHECK_EMAIL_VERIFICATION`: Set to `True` to require email verification in Keycloak for VPN access.

## How to Use
1. Ensure you have a Keycloak client set up for your Pritunl server.
2. Clone the repository to your Pritunl server.
3. Adjust the parameters in the script as per your Keycloak configuration.
4. Integrate the script into your Pritunl server's user authentication flow.

## Contribution
Contributions to this project are welcome! Please feel free to fork the repository, make your changes on a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
