# test_climatesimulator.py
"""
Tests for ClimateSimulator module.
"""

import unittest
from climatesimulator import ClimateSimulator

class TestClimateSimulator(unittest.TestCase):
    """Test cases for ClimateSimulator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ClimateSimulator()
        self.assertIsInstance(instance, ClimateSimulator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ClimateSimulator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
