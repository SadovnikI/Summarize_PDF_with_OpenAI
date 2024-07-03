## Project Title
**PDF Summarization API**

## Objective
Create a REST API that allows users to upload a 1-page PDF file and get a summary of its content. The API is containerized using Docker.

## Setup and Usage Instructions

### Prerequisites
- Docker installed on your machine.
- Python 3.10 or higher
- An OpenAI API key.

### Installation
1. **Clone the Repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a `.env` file:**
    ```sh
    touch .env
    ```
    Add your OpenAI API key to the `.env` file:
    ```sh
    OPENAI_API_KEY=your_openai_api_key
    ```

3. **Build Docker Image and run the Docker Container:**
    ```sh
    docker-compose up --build
    ```

### API Endpoints
#### POST /summarize
- **Description:** Accepts a PDF file upload and returns a summary of its content.
- **Request:**
    ```sh
    curl -X POST http://localhost:8000/summarize -F 'file=@path_to_your_pdf_file'
    ```
- **Response:**
    ```json
    {
      "summary": "This is the summarized content of the PDF."
    }
    ```
  
### Using FastAPI Swagger UI
FastAPI provides a built-in interactive API documentation using Swagger UI. To access it:

1. **Run the Application:**
    Make sure your Docker container is running:
    ```sh
    docker-compose up
    ```

2. **Open Swagger UI:**
    Open your web browser and go to `http://localhost:8080/docs`.

3. **Interact with the API:**
    You can test the `POST /summarize` endpoint directly from the Swagger UI by uploading a PDF file and receiving the summary in response.


## **Access the API:**

The API will be accessible at `http://localhost:8080`.

