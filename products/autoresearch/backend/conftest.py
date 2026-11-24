from collections.abc import Iterator

import pytest
from unittest.mock import patch


@pytest.fixture(autouse=True)
def _autoresearch_limits_as_on_cloud() -> Iterator[None]:
    # Self-hosted, single-tenant fork: the limits are uncapped off Cloud, and upstream's tests assert the Cloud limits.
    with patch("products.autoresearch.backend.limits.is_cloud", return_value=True):
        yield
