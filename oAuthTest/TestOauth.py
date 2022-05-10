from requests_oauth2.services import OAuth2
google_auth = OAuth2(
    client_id = "k4IQRJNFAcMoXwRuSjpZ6S17Cx8W",
    client_secret = "7c80eecc-2b56-4aaf-8c0b-b2644cfada81",
    redirect_uri = 'http://localhost:5000/redirect',
)

authorization_url = google_auth.authorize_url(
    scope = "read:vat write:vat",
    response_type="code",
)

