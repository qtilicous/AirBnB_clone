"""
Empty __init__.py file for the models module.
"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()
storage.reload()
