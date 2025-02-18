# Joke-Service API
This is a Flask-based application that provides an API for retrieving random jokes from https://jokeapi.dev. The API is documented with an OpenAPI specification (Swagger), and you can use Swagger UI to interact with the API in a user-friendly way.

## Features
- Endpoint /api/jokes/random: Retrieves a random joke in JSON format.
- OpenAPI specification: Documentation available through Swagger UI at /swagger.
- Modeling JSON responses: The API response contains two fields: setup (the question) and punchline (the punchline of the joke).

## Prerequisites
To run the project, you will need:

* Python 3.7 or later.
* Pip (Python Package Installer).

## Installation
Clone this repo:

```bash
git clone <repo-url>
cd joke-service
```
Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```
Activate the virtual environment:

On Windows:

```bash
.\.venv\Scripts\activate
```
On macOS/Linux:

```bash
source .venv/bin/activate
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application
To start the application, run the following command:

```bash
python app.py
```

The application will start on http://localhost:5000 by default.

## Build and Run the Application with Docker
To run the application in a Docker container, you can follow these steps. This makes it easy to deploy the application without having to manually manage dependencies or environment settings.

### Step 1: Build the Docker Image
Make sure you have Docker installed on your machine. If you don't have Docker, you can download and install it from docker.com.

In the root folder of the project, where your Dockerfile is located, run the following command to build the Docker image:

```bash
docker build -t joke-service .
```

joke-service is the name of the Docker image that will be created.
The dot (.) indicates that the build process should run in the current directory, where the Dockerfile and all other project files are located.

### Step 2: Run the Docker Container
Once the image is built, you can start the application in a Docker container with the following command:

```bash
docker run -p 5000:5000 joke-service
```
-p 5000:5000 maps port 5000 on your machine to port 5000 in the container. This allows you to access the application at http://localhost:5000 in your browser.

joke-service is the name of the image we built in the previous step.

## Access the API and Swagger UI
The API is available at:
http://localhost:5000/api/jokes/random

Swagger UI, which provides interactive documentation, is available at:
http://localhost:5000/swagger

## API Endpoint
### /api/jokes/random (GET)
#### Description
Retrieves a random joke.

#### Response
200 OK
```json
{
  "setup": "Why don’t skeletons fight each other?",
  "punchline": "They don’t have the guts."
}
```
## Documentation
Swagger UI will generate the OpenAPI specification and provide a detailed description of all available endpoints. You can interact with the API directly from Swagger UI.

## License
This project is licensed under the MIT License.