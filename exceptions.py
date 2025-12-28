# exceptions.py
class DataLoadException(Exception):
    """Raised when CSV or input data is invalid"""
    pass

class MappingException(Exception):
    """Raised when a test point cannot be mapped"""
    pass

class DatabaseException(Exception):
    """Raised for database operation errors"""
    pass
