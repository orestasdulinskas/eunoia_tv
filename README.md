<h1 align='center'>Eunoia TV</h1>
<h3 align='center'>Orestas Dulinskas</h3>
<h4 align='center'>August 2024</h4>

## Description
**Eunoia TV** is a static website that displays random inspiring content, such as GIFs and images, celebrating human achievements in sports, technology, and other domains. The content is dynamically pulled from a Tumblr blog using the Tumblr API. The backend, built using Flask and hosted on AWS Lambda, retrieves and serves the media URLs, while the frontend showcases these images in a continuous loop, changing every 5 seconds.

This project aims to inspire and celebrate the power of human innovation and creativity.

## Features
- Displays random GIFs and images every 5 seconds.
- Content is dynamically fetched from a Tumblr blog.
- The backend fetches post URLs using Tumblr's API and provides them to the frontend.
- Hosted on AWS using Lambda, API Gateway, and S3 for a serverless architecture.
- Flask API with CORS support to allow cross-origin requests from the frontend.

## Architecture
The project consists of two main components:
1. **Backend**: Flask-based API hosted on AWS Lambda, integrated with Tumblr's API to fetch content.
2. **Frontend**: A static HTML, CSS, and JavaScript website hosted on AWS S3, which retrieves data from the backend and displays the media content.

## Technologies Used
- **Backend**: 
  - Flask (Python)
  - Tumblr API for fetching posts
  - AWS Lambda for serverless API hosting
  - API Gateway for routing
  - `requests` library with retry mechanism
  - dotenv for environment variable management

- **Frontend**:
  - HTML, CSS, and JavaScript
  - Hosted on AWS S3
  - Fetch API to get data from the Flask backend
  - Interval-based random content display (updated every 5 seconds)

## Setup

### Backend Setup
1. Clone the repository.
    ```bash
    git clone https://github.com/orestasdulinskas/eunoia_tv.git
    cd eunoia_tv/backend
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file in the backend folder.
    - Add your Tumblr API key:
      ```env
      TUMBLR_API_KEY=your_tumblr_api_key
      ```

4. Run the Flask app locally for testing:
    ```bash
    python app.py
    ```

5. Deploy the Flask app to AWS Lambda

### Frontend Setup
1. Host the frontend files (HTML, CSS, JS) on AWS S3 as a static website.
2. Make sure to update the fetch URL in the HTML file to point to your deployed API Gateway endpoint:
    ```javascript
    fetch('https://your-api-endpoint.amazonaws.com/random-content')
    ```

### Environment Variables
- `TUMBLR_API_KEY`: Your API key for accessing Tumblr's API.

## Running Locally
1. **Backend**: Run the Flask app:
    ```bash
    python app.py
    ```
    This will start the backend server on `http://127.0.0.1:5000/random-content`.

2. **Frontend**: Open the `index.html` file in your browser. The page will automatically fetch content from the local Flask server.

## Deployment
1. **Backend**: Deploy the Flask app using AWS Lambda
2. **Frontend**: Upload the HTML, CSS, and JS files to AWS S3, enabling static website hosting.

## Usage
- Open the website in your browser, and every 5 seconds, a new image or GIF celebrating human achievements will appear.
- The content is pulled dynamically from a Tumblr blog using the backend API.

## Contact
For questions or suggestions, please reach out to orestasdulinskas@gmail.com