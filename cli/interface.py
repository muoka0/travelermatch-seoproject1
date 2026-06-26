from services.gemini_client import map_interest_to_tags, rank_destinations

from services.gemini_client import map_interest_to_tags, rank_destinations



def run_interface():

    print("\n--- Travel Match ---\n")



    budget = input("Budget ($, $$, $$$): ").strip()

    climate = input("Preferred climate: ").strip()

    interests = input("What are your interests? ").strip()



    tags = map_interest_to_tags(interests)



    options_data = [

        {

            "city": "Bali",

            "avg_high": 89.0,

            "avg_low": 69.3,

            "avg_daily_rain_mm": 1.8

        },

        {

            "city": "Bangkok",

            "avg_high": 95.0,

            "avg_low": 75.0,

            "avg_daily_rain_mm": 0.5

        }

    ]



    ranked = rank_destinations(

        {

            "budget": budget,

            "climate": climate,

            "interests": ", ".join(tags)

        },

        options_data

    )



    print("\n--- Top Matches ---\n")

    for r in ranked:

        print(f"{r['city']}: {r['reasoning']}")



    return {

        "budget": budget,

        "climate": climate,

        "interests": interests,

        "tags": tags,

        "ranked": ranked

    