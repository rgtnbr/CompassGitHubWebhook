# sample_test.py

def add(a, b):
    """A simple function to add two numbers."""
    return a + b

def subtract(a, b):
    """A simple function to subtract two numbers."""
    return a - b

# Test cases
if __name__ == "__main__":
    # Test the add function
    assert add(2, 3) == 5, "Addition Test Failed"
    assert add(-1, 1) == 0, "Addition Test Failed"
    
    # Test the subtract function
    assert subtract(5, 3) == 2, "Subtraction Test Failed"
    assert subtract(0, 3) == -3, "Subtraction Test Failed"

    print("All tests passed successfully!")
