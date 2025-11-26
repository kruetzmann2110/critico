"""
Main Critico module
"""


class Critico:
    """
    A class for performing critical analysis and reviews
    """
    
    def __init__(self, name: str = "Critico"):
        """
        Initialize a Critico instance
        
        Args:
            name (str): Name of the critic
        """
        self.name = name
        self.reviews = []
    
    def add_review(self, item: str, rating: int, comment: str = "") -> dict:
        """
        Add a review for an item
        
        Args:
            item (str): The item being reviewed
            rating (int): Rating from 1 to 5
            comment (str): Optional comment about the item
        
        Returns:
            dict: The review that was added
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        review = {
            "item": item,
            "rating": rating,
            "comment": comment,
            "critic": self.name
        }
        self.reviews.append(review)
        return review
    
    def get_reviews(self) -> list:
        """
        Get all reviews
        
        Returns:
            list: A copy of all reviews
        """
        return self.reviews.copy()
    
    def get_average_rating(self) -> float:
        """
        Calculate the average rating of all reviews
        
        Returns:
            float: Average rating, or 0 if no reviews
        """
        if not self.reviews:
            return 0.0
        
        total = sum(review["rating"] for review in self.reviews)
        return total / len(self.reviews)
    
    def __repr__(self):
        return f"Critico(name='{self.name}', reviews={len(self.reviews)})"
