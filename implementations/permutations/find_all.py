class FindAllPermutations:
    """
    Find all permutations of a list of characters.

    Example:
        finder = FindAllPermutations()
        result = finder.permute(['a', 'b', 'c'])
        # Returns: [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'],
        #           ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]
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
        if not chars:
            self.result.append(current[:])
            return

        seen = set()
        for i in range(len(chars)):
            if chars[i] in seen:
                continue
            seen.add(chars[i])
            current.append(chars[i])
            remaining = chars[:i] + chars[i+1:]
            self._backtrack(remaining, current)
            current.pop()
