# auth-api
 Session-Based Auth REST API  This project is a RESTful API service implementing session- based authentication for user sign-up, login, authorization, and token management. The API is built with Django providing secure and scalable user authentication and authorization functionalities.  Features:  User Sign-Up: Create a new user with a secure hashed password.  User Login: Authenticate users and generate tokens.  Token-Based Authorization: Protect endpoints by validating tokens for authenticated access.  Token Revocation: Allow users to logout and revoke tokens to prevent reuse.  Token Refresh: Enable token renewal to keep sessions active without re-login.  Error Handling: Return appropriate status codes and messages for different failure cases.   Technologies: Django for backend logic  Session based authentication for token-based security Mongodb for data storage (configurable)     Project Setup  1. Clone the repository and set up your environment.    2. Use provided curl commands in the README to test each endpoint (sign-up, login, token-protected route access, logout, refresh).    Testing  Unit tests are included to verify authentication flows, available in the tests/ directory.  This repository demonstrates essential practices in building secure, token-based authentication systems, making it ideal for developers learning backend security concepts or building scalable APIs. 
Features:  User Sign-Up: Create a new user with a secure hashed password.  User Login: Authenticate users and generate tokens.  Token-Based Authorization: Protect endpoints by validating tokens for authenticated access.  Token Revocation: Allow users to logout and revoke tokens to prevent reuse.  Token Refresh: Enable token renewal to keep sessions active without re-login.  Error Handling: Return appropriate status codes and messages for different failure cases.   Technologies: Django for backend logic  Session based authentication for token-based security Mongodb for data storage (configurable) .
Project Setup  1. Clone the repository and set up your environment.    2. Use provided curl commands in the README to test each endpoint (sign-up, login, token-protected route access, logout, refresh).    Testing Unit tests are included to verify authentication flows, available in the tests/ directory.  
This API allows users to perform authentication actions, including registering, logging in, logging out, logging out from all sessions, and retrieving profile information. Each endpoint can be tested using curl commands as described below.

Requirements
Ensure the API server is running on http://127.0.0.1:8000 before making these requests.

Endpoints and Usage
1. Register a New User
This endpoint registers a new user by providing their email and password. Both password and password2 should match.

bash
Copy code
curl --location 'http://127.0.0.1:8000/api/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "abhay1@gmail.com",
    "password": "12345678",
    "password2": "12345678"
}'
Parameters:

email: The user's email address.
password: The user’s password.
password2: Confirmation of the password (must match password).
2. User Login
This endpoint logs in an existing user, returning an access token for authenticated actions.

bash
Copy code
curl --location 'http://127.0.0.1:8000/api/auth/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "abhay1@gmail.com",
    "password": "12345678"
}'
Parameters:

email: The registered email of the user.
password: The user’s password.
3. User Logout
This endpoint logs out the current session, invalidating the access token.

bash
Copy code
curl --location --request POST 'http://127.0.0.1:8000/api/logout/' \
--header 'Authorization: Bearer <access_token>'
Headers:

Authorization: The access token obtained from the login request, formatted as Bearer <access_token>.
4. Logout from All Sessions
This endpoint logs out the user from all active sessions by invalidating all tokens associated with the account.

bash
Copy code
curl --location --request POST 'http://127.0.0.1:8000/api/logoutall/' \
--header 'Authorization: Bearer <access_token>'
Headers:

Authorization: The access token obtained from the login request, formatted as Bearer <access_token>.
5. Retrieve User Profile
This endpoint retrieves the authenticated user's profile information.

bash
Copy code
curl --location 'http://127.0.0.1:8000/api/profile/' \
--header 'Authorization: Bearer <access_token>'
Headers:

Authorization: The access token obtained from the login request, formatted as Bearer <access_token>.
Notes
Replace <access_token> in each command with the actual token obtained from the login response.
Ensure each endpoint requiring authorization includes the correct bearer token.
