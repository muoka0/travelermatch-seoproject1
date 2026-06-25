INTEREST_MAPPING_PROMPT = """
The user is looking for travel destinations and described their interests as:

"{user_input}"

Map these interests to relevant travel tags from this list:
temples, rice-terraces, surfing, yoga, food, beaches, hiking, nightlife, shopping, museums, history, culture, wildlife, adventure, wellness,
beaches, street-food, markets, trekking, elephants, colonial-architecture, salsa, cenotes, vintage-cars, rum, jazz, anime, cherry-blossoms, thrifting, technology, shrines, fashion, kpop,
bbq, palaces, hiking, art-museums, wine, cafes, romance, murals, tacos, aztec-ruins, pyramids, mezcal, views, sight-seeing, broadway, diversity, skyline, techno,
murals, cold-war-history, street-art, beer, lgbtq, tango, steak, football, soccer, dance, gymnastics, geishas, bamboo, zen-gardens, tea-ceremony, gaudi, tapas, fado, trams, 
souks, spices, desert, hammams, colosseum, pasta, vatican, ancient-history, pharaohs, nile, table-mountain, safari, wine-farms, acropolis,
philosophy, game-of-thrones, walled-city, sailing, northern-lights, geysers, hot-springs, volcanoes, dog-sledding, fjords, skiing, nature,
adventure, culture, history, architecure, diving, live-music, festivals, beauty, community, livliness, 
energy, relaxing, spa, wellness, vintage

Return only a comma-separated list of matching tags. Don't include extra text.
"""

RANKING_PROMPT = """

You are a travel recommendation assistant. 

The user is looking for destinations with:
- Budget: {budget}
- Climate preference: {climate}
- Interests: {interests}

Here are the candidate destinations with weather data:
{options_data}

Rank the top 3 destinations that best match the user's preferences. 
Return a JSON array with exactly 3 objects in this format:

[
    {{
        "city": "City Name",
        "reasoning": "2-3 sentence explanation of why this city matches the user's budget, climate, and interests."
    }},
    {{
        "city": "City Name", 
        "reasoning": "..."
    }},
    {{
        "city": "City Name",
        "reasoning": "..."
    }}
]

Return only the JSON array. Do not include markdown, backticks, or extra text.
"""