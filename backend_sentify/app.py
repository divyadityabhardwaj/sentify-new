# backend_sentify/app.py
from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # Import VADER
from flask_cors import CORS
import re
import os
from dotenv import load_dotenv  # Import dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# YouTube API setup
API_KEY = os.getenv('YOUTUBE_API_KEY')  # Get API key from environment variable
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()  # Initialize VADER

def get_youtube_comments(video_id):
    comments = []
    try:
        # Retrieve comments from the YouTube video
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=100  # Adjust as needed
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        # Handle pagination if there are more comments
        while 'nextPageToken' in response:
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                maxResults=100,
                pageToken=response['nextPageToken']
            ).execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)

    except Exception as e:
        print(f"An error occurred while fetching comments: {e}")

    return comments

def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    regex = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)([^&]{11})'
    match = re.search(regex, url)
    return match.group(1) if match else None

@app.route('/analyze_comments', methods=['POST'])
def analyze_comments():
    data = request.json
    video_url = data.get('video_url')

    # Extract video ID from the URL
    video_id = extract_video_id(video_url)

    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    # Get comments from the YouTube video
    comments = get_youtube_comments(video_id)

    if not comments:
        return jsonify({"error": "No comments found for this video."}), 404

    # Analyze sentiments using VADER
    positive_count = 0
    negative_count = 0

    for comment in comments:
        score = sia.polarity_scores(comment)  # Get VADER sentiment scores
        if score['compound'] >= 0.05:
            positive_count += 1
        elif score['compound'] <= -0.05:
            negative_count += 1

    total_comments = len(comments)
    positive_percentage = (positive_count / total_comments) * 100 if total_comments > 0 else 0
    negative_percentage = (negative_count / total_comments) * 100 if total_comments > 0 else 0

    # Prepare the response
    response = {
        'positive_percentage': positive_percentage,
        'negative_percentage': negative_percentage,
        'total_comments': total_comments
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
