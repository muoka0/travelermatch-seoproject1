import unittest
from unittest.mock import patch, MagicMock 
from services.gemini_client import map_interest_to_tags, rank_destinations 

class TestMapInterestToTags(unittest.TestCase):
    @patch("services.gemini_client.client")
    def test_returns_list_of_tags(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = "food, temples, beaches"
        mock_client.models.generate_content.return_value = mock_response

        result = map_interest_to_tags("I love eating and visiting temple")
        self.assertIsInstance(result, list)
        self.assertIn("food", result)
        self.assertIn("temples", result)

    @patch("services.gemini_client.client")
    def test_tags_are_lowercase(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = "Food, Beaches, NIGHTLIFE"
        mock_client.models.generate_content.return_value = mock_response

        result = map_interest_to_tags("food and beach vibes")
        for tag in result:
            self.assertEqual(tag, tag.lower())

    @patch("services.gemini_client.client")
    def test_whitespace_stripped_from_tags(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = " food   ,  beaches   , nightlife  "
        mock_client.models.generate_content.return_value = mock_response 

        result = map_interest_to_tags("food and beaches")
        self.assertIn("food", result)
        self.assertIn("beaches", result)
        self.assertIn("nightlife", result)

    @patch("services.gemini_client.client")
    def test_empty_gemini_response_returns_empty_list(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = ""
        mock_client.models.generate_content.return_value = mock_response
        
        result = map_interest_to_tags("something")
        self.assertEqual(result, [])

class TestRankDestinations(unittest.TestCase):
    def setUp(self):
        self.user_inputs = {
            "budget": "$$",
            "climate": "tropical",
            "interests": "food, beaches"
        }
        self.options_data = [
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

    @patch("services.gemini_client.client")
    def test_returns_list(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = '''[
            {"city": "Bali", "reasoning": "Great for food and beaches."},
            {"city": "Bangkok", "reasoning": "Amazing street food."},
            {"city": "Cartagena", "reasoning": "Beautiful beaches."}
        ]'''
        mock_client.models.generate_content.return_value = mock_response

        result = rank_destinations(self.user_inputs, self.options_data)
        self.assertIsInstance(result, list)

    @patch("services.gemini_client.client")
    def test_returns_city_and_reasoning(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = '''[
            {"city": "Bali", "reasoning": "Perfect tropical destinations."},
            {"city": "Bangkok", "reasoning": "Great street food."},
            {"city": "Cartagena", "reasoning": "Beauitful beaches."}
        ]'''
        mock_client.models.generate_content.return_value = mock_response
        result = rank_destinations(self.user_inputs, self.options_data)
        for item in result:
            self.assertIn("city", item)
            self.assertIn("reasoning", item)
    def test_empty_options_returns_empty_list(self):
        result = rank_destinations(self.user_inputs, [])
        self.assertEqual(result, [])

    def test_skips_error_entries(self):
        bad_data = [{"city": "Unknown", "error": "City not found"}]
        result = rank_destinations(self.user_inputs, bad_data)
        self.assertEqual(result, [])
    @patch("services.gemini_client.client")
    def test_invalid_returns_empty_list(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = "this is not json"
        mock_client.models.generate_content.return_value = mock_response
        
        result = rank_destinations(self.user_inputs, self.options_data)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()