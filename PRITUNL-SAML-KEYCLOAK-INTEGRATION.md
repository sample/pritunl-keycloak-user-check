# How to Configure Pritunl and Keycloak Integration

This guide details the steps required to configure Keycloak and integrate it with Pritunl Enterprise, including optional configuration for the pritunl-keycloak-user-check.

### Table of Contents

1. Configure Keycloak
2. Configure Pritunl Enterprise to Use Keycloak
3. Optional: Configure pritunl-keycloak-user-check

## Configure Keycloak

Set up a new client in Keycloak with the following example configuration:

### Client Configuration:

1. Client Type: *SAML*
2. Client ID: *pritunl*
3. Name: *Pritunl SSO Client*
4. Valid Redirect URIs: *https://auth.pritunl.com/v1/callback/saml*
5. Name ID Format: *email*
6. Force Name ID Format: *On*
7. Force POST Binding: *On*
8. Include AuthnStatement: *Off*
9. Sign Documents: *On*
10. Front Channel Logout: *On*

Keys Configuration:
1. Client Signature Required: *Off*

Client Scopes:
Navigate to the "pritunl-dedicated" scope and select Configure a new mapper.
Choose User Property.
1. Set Name: *email*
2. Choose Property: *email*
3. Set Friendly Name: *Email*
4. Set SAML Attribute Name: *email*
5. Set SAML Attribute NameFormat: *Basic*
6. Click *Save*.

## Configure Pritunl Enterprise to Use Keycloak

To configure Pritunl Enterprise, gather the following information from Keycloak:

### SAML Certificate:
Obtain from https://<keycloak_url>/realms/<your_realm>/protocol/saml/descriptor or from Realm Settings -> Keys -> RS256 Certificate button.
Ensure to wrap the certificate with **-----BEGIN CERTIFICATE-----** and **-----END CERTIFICATE-----**.

### SAML Sign-on URL:
Example: https://<keycloak_url>/realms/<your_realm>/protocol/saml

### SAML Issuer URL:
Example: https://<keycloak_url>/realms/<your_realm>

### Default Single Sign-On Organization:
Select your organization, only one can be chosen.

### Single Sign-On Settings:
Set to SAML in Pritunl settings.

Example Configuration:
![pritunl-saml-configuration](https://github.com/sample/pritunl-keycloak-user-check/assets/354018/91190ef4-7eb7-4036-a975-b33a04b4a320)

## Optional: Configure pritunl-keycloak-user-check 
Use documentation from README.md in this repository.
