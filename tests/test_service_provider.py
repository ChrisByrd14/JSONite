from unittest.mock import Mock

from masonite.provider import ServiceProvider
import pytest

from py2js.Javascript import Javascript
from py2js.JavascriptProvider import JavascriptProvider


def test_service_provider_exists():
    assert issubclass(JavascriptProvider, ServiceProvider)


def test_service_provider_register_method_binds_to_container():
    app = Mock()
    provider = JavascriptProvider()
    provider.app = app
    provider.register()
    app.bind.assert_called_once()


def test_service_provider_passes_service_class_to_container():
    app = Mock()
    provider = JavascriptProvider()
    provider.app = app
    provider.register()
    app.bind.assert_called_with("Javascript", Javascript)
