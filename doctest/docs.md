So before the function was implemented, I just had tests as I do with unittests for TDD.


# Define the tests

```python
import doctest

def post_date(content):
    """
    Extract the date from the content
    >>> post_date('Date: 2019-10-31')
    '2019-10-31'
    >>> post_date('Date: foobar')
    Traceback (most recent call last):
        ...
    ValueError: time data 'foobar' does not match format '%Y-%m-%d'
    """
    date = ''
    return date

if __name__ == "__main__":
    doctest.testmod()
```

and running the tests with `python doctest_tdd.py` would output:

```
**********************************************************************
File "doctest_tdd.py", line 8, in __main__.post_date
Failed example:
    post_date('Date: 2019-10-31')
Expected:
    '2019-10-31'
Got:
    ''
**********************************************************************
File "doctest_tdd.py", line 10, in __main__.post_date
Failed example:
    post_date('Date: foobar')
Expected:
    Traceback (most recent call last):
        ...
    ValueError: time data 'foobar' does not match format '%Y-%m-%d'
Got:
    ''
**********************************************************************
1 items had failures:
   2 of   2 in __main__.post_date
***Test Failed*** 2 failures.
```


# Implement parsing

```python
import doctest

def post_date(content):
    """
    Extract the date from the content

    >>> post_date('Date: 2019-10-31')
    '2019-10-31'
    >>> post_date('Date: foobar')
    Traceback (most recent call last):
        ...
    ValueError: time data 'foobar' does not match format '%Y-%m-%d'
    """
    date = content.split(':')[1].strip()
    return date

if __name__ == "__main__":
    doctest.testmod()
```

Then running the tests.

```
**********************************************************************
File "doctest_tdd.py", line 10, in __main__.post_date
Failed example:
    post_date('Date: foobar')
Expected:
    Traceback (most recent call last):
        ...
    ValueError: time data 'foobar' does not match format '%Y-%m-%d'
Got:
    'foobar'
**********************************************************************
1 items had failures:
   1 of   2 in __main__.post_date
***Test Failed*** 1 failures.
```

# Implement the format checker

Lool at the final code above.
Let's run the tests one last time.

Nothing. All tests have passed.

# Verbose?
If we want to have more details: `python doctest_tdd.py -v`

```
Trying:
    post_date('Date: 2019-10-31')
Expecting:
    '2019-10-31'
ok
Trying:
    post_date('Date: foobar')
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: time data 'foobar' does not match format '%Y-%m-%d'
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.post_date
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```
