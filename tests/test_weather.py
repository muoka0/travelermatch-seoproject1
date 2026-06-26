import unittest
from unittest.mock import patch, MagicMock 
from services.weather_client import get_coordinates, get_weather, get_weather_for_locations

class TestGetCoordinates(unittest.TestCase):
    @patch("services.weather_client.requests.get")
    def test_returns_lat_lon(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [{"latitude": -8.65, "longitude": 115.22}]
        }
        mock_get.return_value = mock_response

        lat, lon = get_coordinates("Bali")
        self.assertEqual(lat, -8.65)
        self.assertEqual(lon, 115.22)
    @patch("services.weather_client.requests.get")
    def test_city_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        lat, lon = get_coordinates("TestCity")
        self.assertIsNone(lat)
        self.assertIsNone(lon)

    @patch("services.weather_client.requests.get")
    def test_returns_first_result(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {"latitude": -8.65, "longitude": 115.22},
                {"latitude": 10.0, "longitude": 20.0}
            ]
        }
        mock_get.return_value = mock_response

        lat, lon = get_coordinates("Bali")
        self.assertEqual(lat, -8.65)
        self.assertEqual(lon, 115.22)

class TestGetWeather(unittest.TestCase):
    @patch("services.weather_client.requests.get")
    def test_returns_weather_dict(self, mock_get):
        mock_geo = MagicMock()
        mock_geo.json.return_value = {
            "results": [{"latitude": -8.65, "longitude": 115.22}]
        }
        mock_weather = MagicMock()
        mock_weather.json.return_value = {
            "daily": {
                "temperature_2m_max": [89.0],
                "temperature_2m_min": [70.0],
                "precipitation_sum": [1.5]
            }
        }
        mock_get.side_effect = [mock_geo, mock_weather]

        result = get_weather("Bali", "2023-01-01", "2023-01-07")
        self.assertEqual(result["start_date"], "2023-01-01")
        self.assertEqual(result["end_date"], "2023-01-07")

class TestGetWeatherForLocations(unittest.TestCase):
    @patch("services.weather_client.get_weather")
    def test_returns_list_for_multiple_cities(self, mock_get_weather):
        mock_get_weather.return_value = {
            "city": "Bali",
            "avg_high": 89.0,
            "avg_low": 69.3,
            "avg_daily_rain_mm": 1.8
        }

        result = get_weather_for_locations(
            ["Bali", "Bangkok"], "2023-01-01", "2023-01-07"
        )
        self.assertEqual(len(result), 2)

    @patch("services.weather_client.get_weather")
    def test_empty_cities_returns_empty_list(self,mock_get_weather):
        result = get_weather_for_locations([], "2023-01-01", "2023-01-07")
        self.assertEqual(result, [])

    @patch("services.weather_client.get_weather")
    def test_calls_get_weather_for_each_city(self, mock_get_weather):
        mock_get_weather.return_value = {"city": "Bali", "avg_high": 89.0}

        get_weather_for_locations(
            ["Bali", "Bangkok", "Cartagena"], "2023-01-01", "2023-01-07"
        )
        self.assertEqual(mock_get_weather.call_count, 3)
if __name__ == "__main__":
    unittest.main()
