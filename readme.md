# Sentify

Sentify is a web application that performs sentiment analysis on YouTube comments using Flask for the backend and Next.js for the frontend. The application retrieves comments from specified YouTube videos and analyzes their sentiment using the VADER sentiment analysis tool.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Retrieve comments from YouTube videos.
- Perform sentiment analysis on the retrieved comments.
- Display sentiment results in a user-friendly interface.

## Technologies Used

- **Backend**: Flask, Flask-CORS, Google API Client, NLTK
- **Frontend**: Next.js, React, Tailwind CSS
- **Database**: None (data is fetched directly from the YouTube API)
- **Environment Variables**: dotenv for managing API keys

## Getting Started

### Prerequisites

- Node.js (for the frontend)
- Python 3.x (for the backend)
- A YouTube Data API key

### Backend Setup

1. Navigate to the `backend_sentify` directory:
   ```bash
   cd backend_sentify
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the `backend_sentify` directory and add your YouTube API key:
   ```plaintext
   YOUTUBE_API_KEY=your_api_key_here
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the `sentify` directory:
   ```bash
   cd sentify
   ```

2. Install the required Node.js packages:
   ```bash
   npm install
   ```

3. Run the Next.js development server:
   ```bash
   npm run dev
   ```

4. Open your browser and go to ----------- to view the application.

## Usage

- Enter a YouTube video URL in the input field and click "Analyze Sentiment" to retrieve and analyze comments.
- The sentiment analysis results will be displayed in a pie chart format.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

