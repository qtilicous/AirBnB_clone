import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        # Save the instance to a JSON file (implementation needed)

    def to_dict(self):
        # Convert instance attributes to a dictionary (implementation needed)
