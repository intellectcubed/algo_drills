class FindAllPermutations:
    """
    TODO: Implement a class that finds all permutations of a list of characters.

    Use backtracking to generate all possible permutations.
    """

    def __init__(self):
        self.result = []

    def permute(self, chars):
        """
        Generate all permutations of the given list of characters.

        Args:
            chars: A list of characters to permute

        Returns:
            A list of all permutations, where each permutation is a list
        """
        if not chars:
            return []

        self.result = []
        self._backtrack(chars, [])
        return self.result

    def _backtrack(self, chars, current):
        """
        Recursive helper function to generate permutations using backtracking.

        Args:
            chars: Remaining characters to permute
            current: Current permutation being built
        """
        # TODO: Implement the backtracking logic
        # Base case: if no more chars, add current to result
        # Recursive case: try each remaining char and recurse
        pass