import pytest
from unittest.mock import patch, MagicMock
import passwordchecker.checkmypass as cmp


class TestPwnedApiCheck:

    def test_password_found(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "1E4C9B93F3F0682250B6CF8331B7EE68FD8:3\n3D4F2BF07DC1BE38B20CD6E46949A1071F:1"

        result = cmp.get_password_leaks_count(mock_response, "1E4C9B93F3F0682250B6CF8331B7EE68FD8")
        assert result == "3"

    def test_password_not_found(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "AAAAABBBBBCCCCC:5"

        result = cmp.get_password_leaks_count(mock_response, "NOTINLIST")
        assert result == 0

    def test_main_calls_api(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = ""

        with patch('passwordchecker.checkmypass.requests.get', return_value=mock_response):
            result = cmp.main(["hello"])
            assert result == 'done!'
