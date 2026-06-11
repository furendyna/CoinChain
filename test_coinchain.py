# test_coinchain.py
"""
Tests for CoinChain module.
"""

import unittest
from coinchain import CoinChain

class TestCoinChain(unittest.TestCase):
    """Test cases for CoinChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinChain()
        self.assertIsInstance(instance, CoinChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
