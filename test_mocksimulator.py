# test_mocksimulator.py
"""
Tests for MockSimulator module.
"""

import unittest
from mocksimulator import MockSimulator

class TestMockSimulator(unittest.TestCase):
    """Test cases for MockSimulator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MockSimulator()
        self.assertIsInstance(instance, MockSimulator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MockSimulator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
