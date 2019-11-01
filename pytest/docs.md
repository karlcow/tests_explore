# Pytest TDD

While [doctest](https://docs.python.org/3.8/library/doctest.html) is part of the system, [pytest](https://docs.pytest.org/en/latest/) introduces a dependency. We need to install pytest.

Let's create an environment for it.
```bash
# These are usually my commands when working on a project.
python -m venv env
source env/bin/activate
pip install --upgrade pip
# finally the install
pip install pytest
```

So we need to add a requirements.txt to the project.

```bash
echo 'pytest' >> requirements.txt
```

# Create tests

No function implemented.

```python
"""
Pytest TDD Example
"""
import pytest

def test_post_date_parsing():
    """Check the date parsing."""
    assert post_date('Date: 2019-10-31') == '2019-10-31'


def test_post_date_wrong_format():
    """Check the format of the file."""
    with pytest.raises(ValueError):
        post_date('Date: foobar')
```

Then let's run the tests.

```bash
pytest pytest/pytest_tdd.py
```

The result is slightly more verbose than in the case of [doctest](../doctest/docs.md). It gives a lot of interesting information about the environment too.

```
================================================================= test session starts =================================================================
platform darwin -- Python 3.7.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0
rootdir: /Users/karl/code/tests_explore
collected 2 items

pytest/pytest_tdd.py FF                                                                                                                         [100%]

====================================================================== FAILURES =======================================================================
_______________________________________________________________ test_post_date_parsing ________________________________________________________________

    def test_post_date_parsing():
        """Check the date parsing."""
>       assert post_date('Date: 2019-10-31') == '2019-10-31'
E       NameError: name 'post_date' is not defined

pytest/pytest_tdd.py:8: NameError
_____________________________________________________________ test_post_date_wrong_format _____________________________________________________________

    def test_post_date_wrong_format():
        """Check the format of the file."""
        with pytest.raises(ValueError):
>           post_date('Date: foobar')
E           NameError: name 'post_date' is not defined

pytest/pytest_tdd.py:14: NameError
================================================================== 2 failed in 0.07s ==================================================================

```

# Implement the date parsing

```python
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
```

Then let's run the test again.

```bash
pytest pytest/pytest_tdd.py
```

One failure and one test passing, as expected.

```
================================================================= test session starts =================================================================
platform darwin -- Python 3.7.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0
rootdir: /Users/karl/code/tests_explore
collected 2 items

pytest/pytest_tdd.py .F                                                                                                                         [100%]

====================================================================== FAILURES =======================================================================
_____________________________________________________________ test_post_date_wrong_format _____________________________________________________________

    def test_post_date_wrong_format():
        """Check the format of the file."""
        with pytest.raises(ValueError):
>           post_date('Date: foobar')
E           Failed: DID NOT RAISE <class 'ValueError'>

pytest/pytest_tdd.py:20: Failed
============================================================= 1 failed, 1 passed in 0.06s =============================================================
```

# Implement date format checking

We implement the format checker.

```python
"""
Pytest TDD Example
"""
import pytest
import datetime

def post_date(content):
    """Extract the date from the content."""
    date = content.split(':')[1].strip()
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return date
    except Exception as error:
        raise error


def test_post_date_parsing():
    """Check the date parsing."""
    assert post_date('Date: 2019-10-31') == '2019-10-31'


def test_post_date_wrong_format():
    """Check the format of the file."""
    with pytest.raises(ValueError):
        post_date('Date: foobar')
```

Then we run the tests.

```bash
pytest pytest/pytest_tdd.py
```

Everything passes and we get the information that everything is alright.

```
================================================================= test session starts =================================================================
platform darwin -- Python 3.7.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0
rootdir: /Users/karl/code/tests_explore
collected 2 items

pytest/pytest_tdd.py ..                                                                                                                         [100%]

================================================================== 2 passed in 0.01s ==================================================================
```

That's it!