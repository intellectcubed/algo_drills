class FindAllPermutations:
    """
    TODO: Implement a class that finds all permutations of a list of characters.

    Use backtracking to generate all possible permutations.
    """

    def __init__(self):
        self.result = set()

    def permute(self, chars):
        """
        Generate all permutations of the given list of characters.

        Args:
            chars: A list of characters to permute

        Returns:
            A list of all permutations, where each permutation is a list
        """        
