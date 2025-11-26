"""
Tests for the Critico class
"""
import unittest
from critico import Critico


class TestCritico(unittest.TestCase):
    """Test cases for Critico class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.critic = Critico("Test Critic")
    
    def test_initialization(self):
        """Test Critico initialization"""
        self.assertEqual(self.critic.name, "Test Critic")
        self.assertEqual(len(self.critic.reviews), 0)
    
    def test_add_review(self):
        """Test adding a review"""
        review = self.critic.add_review("Test Item", 5, "Excellent!")
        self.assertEqual(review["item"], "Test Item")
        self.assertEqual(review["rating"], 5)
        self.assertEqual(review["comment"], "Excellent!")
        self.assertEqual(review["critic"], "Test Critic")
        self.assertEqual(len(self.critic.reviews), 1)
    
    def test_add_review_invalid_rating(self):
        """Test adding a review with invalid rating"""
        with self.assertRaises(ValueError):
            self.critic.add_review("Test Item", 6)
        with self.assertRaises(ValueError):
            self.critic.add_review("Test Item", 0)
    
    def test_get_reviews(self):
        """Test getting all reviews"""
        self.critic.add_review("Item 1", 4)
        self.critic.add_review("Item 2", 5)
        reviews = self.critic.get_reviews()
        self.assertEqual(len(reviews), 2)
    
    def test_average_rating_empty(self):
        """Test average rating with no reviews"""
        self.assertEqual(self.critic.get_average_rating(), 0.0)
    
    def test_average_rating(self):
        """Test average rating calculation"""
        self.critic.add_review("Item 1", 4)
        self.critic.add_review("Item 2", 5)
        self.critic.add_review("Item 3", 3)
        self.assertEqual(self.critic.get_average_rating(), 4.0)
    
    def test_repr(self):
        """Test string representation"""
        repr_str = repr(self.critic)
        self.assertIn("Test Critic", repr_str)
        self.assertIn("reviews=0", repr_str)


if __name__ == "__main__":
    unittest.main()
