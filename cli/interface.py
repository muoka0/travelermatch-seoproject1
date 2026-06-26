from db.connection import SessionLocal
from db.queries.read import get_unique_climates, get_all_interests

def run_interface():
    print(r"""
=============================================================
████████╗██████╗  █████╗ ██╗   ██╗███████╗██╗     ███████╗██████╗
╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔════╝██║     ██╔════╝██╔══██╗
   ██║   ██████╔╝███████║██║   ██║█████╗  ██║     █████╗  ██████╔╝
   ██║   ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║     ██╔══╝  ██╔══██╗
   ██║   ██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

                    ✈️  TravelerMatch 🌍
          Find your next destination with AI.
=============================================================
""")

    print("Please enter your travel preferences.\n")

    session = SessionLocal()

    climates = get_unique_climates(session)
    climate_options = list(set(climates))[:10]

    interests = get_all_interests(session)
    interest_options = [i.interest for i in interests][:10]

    budget = input("Select Your Desired Budget ($, $$, $$$): ").strip()
    start_date = input("Select Trip Start date (YYYY-MM-DD): ").strip()
    end_date = input("Select Trip End date (YYYY-MM-DD): ").strip()

    print(f"\n🌤️  Available climates: {', '.join(climate_options)}")
    climate = input("Choose a Preferred climate: ").strip()

    print(f"\n🎯  Example interests: {', '.join(interest_options)}")
    interests = input("What are your interests? ").strip()

    return {
        "budget": budget,
        "start_date": start_date,
        "end_date": end_date,
        "climate": climate,
        "interests": interests,
    }