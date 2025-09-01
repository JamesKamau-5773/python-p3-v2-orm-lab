# lib/__init__.py
from .config import CONN, CURSOR

# Import models after config to avoid circular imports
from .department import Department
from .employee import Employee
from .review import Review

__all__ = ['CONN', 'CURSOR', 'Department', 'Employee', 'Review']