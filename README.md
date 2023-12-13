# pritunl-keycloak-user-check

## Description
The `pritunl-keycloak-user-check` is a plugin for Pritunl that checks if a user is available in Keycloak. It enhances the security and flexibility of VPN access management by leveraging Keycloak's authentication system. This repository also includes documentation on integrating Pritunl SSO with Keycloak.

## What the Script Does
The script acts as a middleware between Pritunl and Keycloak, performing real-time user status checks during VPN connection attempts. It ensures that:
- Only users who exist in Keycloak and are not blocked are allowed to access the Pritunl VPN.
- Users blocked with unverified email (optional check) are denied VPN access.

## Configuration Parameters
Before deploying the script, you need to adjust several parameters to match your Keycloak and Pritunl setup:

- `KEYCLOAK_URL`: The URL of your Keycloak instance.
- `REALM`: The realm in Keycloak where your users are managed.
- `CLIENT_ID`: The client ID for the Keycloak client used for authentication.
- `CLIENT_SECRET`: The client secret associated with your Keycloak client.
- `DEBUG`: Set to `True` for detailed logging, useful for debugging.
- `SEARCH_BY_EMAIL`: Set to `True` to search users by email, `False` to search by username.
- `CHECK_EMAIL_VERIFICATION`: Set to `True` to require email verification in Keycloak for VPN access.
- 
## Installation

Follow these steps to deploy the `pritunl-keycloak-user-check` script on your Pritunl server:

## How to Use
1. Ensure you have a Keycloak client set up for your Pritunl server.
2. Place the script to the Pritunl plugins directory. By default, this directory is `/var/lib/pritunl/plugins`.
3. Adjust the parameters in the script as per your Keycloak configuration.
4. sudo `systemctl restart pritunl`.
5. Check the Pritunl logs to ensure that the plugin is loaded correctly and functioning as expected `tail /var/log/pritunl.log -n 100`.
6. Test the VPN connection to confirm that the user status checks against Keycloak are functioning correctly. Attempt to connect with a user that. is both enabled and disabled in Keycloak to see if the script behaves as expected.

## How to setup Pritunl SAML integration with keycloak
See [PRITUNL-SAML-KEYCLOAK-INTEGRATON.md](PRITUNL-SAML-KEYCLOAK-INTEGRATON.md) file

## Contribution
Contributions to this project are welcome! Please feel free to fork the repository, make your changes on a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
