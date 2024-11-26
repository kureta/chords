import itertools


def search_binary(n, prefix=None, condition=None):
    if prefix is None:
        prefix = []

    if condition and not condition(prefix):
        return  # Abort if cumulative sum condition fails

    if len(prefix) == n:
        print(prefix)  # Valid list of 3s and 4s
        cumulative_sums = list(i % 12 for i in itertools.accumulate([6] + prefix))
        print(cumulative_sums)  # Cumulative sums
        return

    # Try adding '3' and '4', and then continue the search
    search_binary(n, prefix + [3], condition)
    search_binary(n, prefix + [4], condition)


# Define the condition: Abort if the cumulative sums have duplicates
def condition(prefix):
    # Calculate cumulative sum for the list of integers (prefix)
    cumulative_sums = list(i % 12 for i in itertools.accumulate([6] + prefix))
    # Check for duplicates in cumulative sums
    return len(cumulative_sums) == len(set(cumulative_sums))


# Example usage
# n = 4  # Length of the list of integers (3s and 4s)
# search_binary(n, condition=condition)
