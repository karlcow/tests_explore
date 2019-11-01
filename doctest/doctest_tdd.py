import doctest
import datetime

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
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return date
    except Exception as error:
        raise error


if __name__ == "__main__":
    doctest.testmod()