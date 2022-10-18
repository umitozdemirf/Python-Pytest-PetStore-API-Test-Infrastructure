"""Configuration for pytest runner."""

import pytest

from config.base_config import BaseConfig

pytest_plugins = 'pytester'


def pytest_html_report_title(report):
    report.title = "PetStore API Test Report"


def pytest_configure(config):
    config._metadata["env"] = BaseConfig.env
    config._metadata["Base URL"] = BaseConfig.API_URL
