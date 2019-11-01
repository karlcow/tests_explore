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
    pass

if __name__ == "__main__":
    doctest.testmod()