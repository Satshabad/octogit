"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import unittest
import mock
from mock import patch, DEFAULT
import octogit.config

class ConfigTest(unittest.TestCase):

    @patch('octogit.config.config')
    def test_get_username(self, mock_config):
        octogit.config.get_username()
        mock_config.get.assert_called_once_with('octogit', 'username')
        mock_config.read.assert_called_once_with(octogit.config.CONFIG_FILE)


if __name__ == '__main__':
    unittest.main()
