"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import json
import unittest
import mock
from mock import patch, DEFAULT, MagicMock

import octogit.config
class ConfigTest(unittest.TestCase):

    @patch('octogit.config.config')
    def test_get_username(self, mock_config):
        octogit.config.get_username()
        mock_config.get.assert_called_once_with('octogit', 'username')
        mock_config.read.assert_called_once_with(octogit.config.CONFIG_FILE)

    @patch('octogit.config.fopen')
    @patch.multiple('octogit.config', requests=DEFAULT, config=DEFAULT)
    def test_login(self, mock_open, requests, config):
        return_request = MagicMock()
        return_request.status_code = 201
        return_request.content = '{"token": "dummy_token"}'
        requests.post = MagicMock(return_value=return_request)
        octogit.config.login('name', 'pass')
        requests.post.assert_called_once_with('https://api.github.com/authorizations',
            auth=('name', 'pass'), data= json.dumps({ "note": "octogit",
                        "note_url": "https://github.com/myusuf3/octogit",
                        "scopes": ["repo"]}))




if __name__ == '__main__':
    unittest.main()
