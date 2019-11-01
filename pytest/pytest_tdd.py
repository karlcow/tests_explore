"""
Pytest TDD Example
"""
import pytest

def post_date(content):
    """Extract the date from the content."""
    date = content.split(':')[1].strip()
    return date


def test_post_date_parsing():
    """Check the date parsing."""
    assert post_date('Date: 2019-10-31') == '2019-10-31'


def test_post_date_wrong_format():
    """Check the format of the file."""
    with pytest.raises(ValueError):
        post_date('Date: foobar')