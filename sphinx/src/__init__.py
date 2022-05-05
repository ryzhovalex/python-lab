def func(arg1: int, arg2: bool = False) -> bool:
    """I love Sphinx but i'm not sure.

    Args:
        arg1 (int): Some argument
        arg2 (bool): I love arguments.
    
    Returns:
        Sense of life, i mean boolean.
    """
    if arg1 > 0 and arg2:
        return True
    else:
        return False


def fetch_smalltable_rows(
    table_handle: int,
    keys: str,
    require_all_keys: bool = False,
) -> None:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: 
            An open smalltable.Table instance.
        keys: 
            A sequence of strings representing the key of each table row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: 
            If True only rows with values set for all keys will be returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
    pass


def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/
    """
    pass
