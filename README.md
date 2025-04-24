# g-based
A template for Google-authenticated flask applications.

![g-based](static/g-based.jpg)

## Overview

A very simple template for use as a starting-point for Google-Authenticated (via OAuth 2) web applications.

## Setup

### Google OAuth 2.0
The application relies upon Google's OAuth service for login.

#### 1. Create Google API credentials

* Go to https://console.developers.google.com/
* Create a new project (or pick an existing one)
* Under "APIs & Services → Credentials" click "Create Credentials → OAuth client ID"
  * Note: If you have never before set up API services prior, you may be required to provide app information. In such a case, ensure you select as the audience "External" such that users can log into your app.
* Application type = "Web application"
* Add "Authorized redirect URIs", e.g.
  * http://localhost:8080/auth/callback
* Copy the Client ID and Client Secret

#### 2. Place secrets in your env variables

* Create a `.env` file in the root directory that includes this content. The `FLASK_SECRET_KEY` should be a secure, lenghty, random string.

```
GOOGLE_CLIENT_ID: your‑google‑client‑id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET: your‑google‑client‑secret
FLASK_SECRET_KEY: some‑random‑string
```