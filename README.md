# TravelerMatch

## Overview

A command-line travel recommendation system that helps users discover personalized travel destinations based on their preferences. TravelerMatch acts as a CLI companion for travel planning, taking in user constraints such as budget, travel dates, climate preferences, and free-form interests, then transforming them into structured insights using AI-powered natural language processing.

The system integrates a multi-stage recommendation pipeline that combines a structured SQLite database of destinations and interests, AI-based interest normalization using the Gemini API, real-time weather validation via external weather APIs, and a final AI ranking stage to ensure recommendations are both relevant and practical for the user’s selected travel window.