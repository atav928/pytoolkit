"""File Mock."""

import unittest
from unittest import mock
from unittest.mock import mock_open

from pytoolkit.files import get_var_dir, read_yaml


class TestReadYaml(unittest.TestCase):
    @mock.patch("builtins.open", mock_open(read_data="data"))
    @mock.patch("pathlib.Path.is_file")
    def test_read_yaml(self, patched_isfile) -> None:
        print("Testing Yaml Read.")
        # valid file case
        patched_isfile.return_value = True
        result = read_yaml("some_file.yaml")
        self.assertEqual("data", result)

    def test_get_var_dir(self):
        self.assertIs(type(get_var_dir()), str)
