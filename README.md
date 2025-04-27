# g-based
A template for Google-authenticated flask applications.

![g-based](static/g-based.jpg)

## Overview

A very simple template for use as a starting-point for Google-Authenticated (via OAuth 2) web applications.

## Setup

The application relies upon Google's OAuth service for login.

### 1. Download and Install Docker

First, download and install [Docker Desktop](https://www.docker.com).

### 2. Clone This Repo

Second, in the folder of your choosing, execute `gh repo clone guyewhite/g-based`.

### 3. Create Google API credentials

* Go to https://console.developers.google.com/
* Create a new project (or pick an existing one)
* Under "APIs & Services → Credentials" click "Create Credentials → OAuth client ID"
  * Note: If you have never before set up API services prior, you may be required to provide app information. In such a case, ensure you select as the audience "External" such that users can log into your app.
* Application type = "Web application"
* Add "Authorized redirect URIs", e.g.
  * http://localhost:8080/auth/callback
* Copy the Client ID and Client Secret

### 4. Place secrets in your env variables

* Create a `.env` file in the root directory that includes this content. The `FLASK_SECRET_KEY` should be a secure, lengthy, random string.

```
GOOGLE_CLIENT_ID: your‑google‑client‑id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET: your‑google‑client‑secret
FLASK_SECRET_KEY: some‑random‑string
```

Please note that your CLI may be set to hide files with a `.` (dot) at the front of the filename.

## Running

Once the above steps have been completed, you can execute the following command:

`docker compose up --build`

Then, with your web browser, browse to `http://localhost:8080`. If an error occurs, best to ensure that you have completed the setup steps above.