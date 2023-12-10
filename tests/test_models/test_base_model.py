import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        # Test creation of a BaseModel instance
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_attribute_assignment(self):
        # Test attribute assignment
        obj = BaseModel()
        obj.name = "Test Object"
        self.assertEqual(obj.name, "Test Object")

        def test_to_dict_method(self):
            # Test the to_dict method
            obj = BaseModel()
            obj.name = "Test Object"
            obj_dict = obj.to_dict()

            self.assertIn('id', obj_dict)
            self.assertIn('created_at', obj_dict)
            self.assertIn('updated_at', obj_dict)
            self.assertIn('name', obj_dict)

            self.assertEqual(obj_dict['id'], obj.id)
            self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
            self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
            self.assertEqual(obj_dict['name'], 'Test Object')


        expected_dict = {
            'id': obj.id,
            'created_at': obj.created_at.isoformat(),
            'updated_at': obj.updated_at.isoformat(),
            'name': 'Test Object'
        }

        self.assertEqual(obj_dict, expected_dict)

    # Add more tests as needed for BaseModel and other classes


if __name__ == '__main__':
    unittest.main()
