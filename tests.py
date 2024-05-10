from service import _get_trends
from unittest import mock

#  It's impossible to test due to the lack of data,
def test_get_trends_with_success():
    mock_api = mock.Mock()
    mock_api.get_place_trends.return_value = []
    trends = _get_trends(woe_id=1000, api=mock_api)
    assert 1 == 1