# TravelerMatch

A command-line travel recommendation system that helps users discover personalized travel destinations based on their preferences. TravelerMatch acts as a CLI companion for travel planning, taking in user constraints such as budget, travel dates, climate preferences, and free-form interests, then transforming them into structured insights using AI-powered natural language processing.

The system integrates a multi-stage recommendation pipeline that combines a structured SQLite database of destinations and interests, AI-based interest normalization using the Gemini API, real-time weather validation via external weather APIs, and a final AI ranking stage to ensure recommendations are both relevant and practical for the user’s selected travel window.

## Features
* **AI-Powered Recommendations:** Uses Google's Gemini API to generate personalized destination recommendations based on user preferences.
* **Smart Interest Mapping:** Converts natural language interests (e.g., "I like hiking and nature") into standardized destination tags before recommendation generation.
* **Jaccard Similarity Scoring:** Measures overlap between a user's normalized interests and each destination's associated interests, providing an objective similarity score before AI ranking.
* **Intelligent Caching:** Previously generated recommendations are cached using a canonical query hash, significantly reducing duplicate Gemini API calls.
* **Constraint-Based Filtering:** Narrows destinations using user-selected budget and climate before AI ranking, improving both speed and recommendation quality.
* **User-Friendly CLI:** Simple terminal interface that guides users through trip planning with suggested climates and interests.


## How It Works
* **Frontend (CLI):** Collects user constraints such as budget, travel dates, preferred climate, and interests. Includes a custom ASCII art interface for an engaging user experience.
* **Backend:** Built with Python, managing the recommendation pipeline, API calls, response caching, and database operations.
* **API Integrations:** Integrates the Open-Meteo API for real-time weather forecasts and the Google Gemini API to normalize user interests and generate personalized destination recommendations.
* **Database Filtering:** Uses SQLite and SQLAlchemy to efficiently filter destinations based on user-selected constraints such as budget and climate before ranking.
* **Destination Ranking:** Computes the Jaccard Similarity score between the user's normalized interests and each destination's associated interests to identify the best matches.

