def calculate_result(operation, values):
    """
    Performs a calculation based on the operation and values.
    
    Args:
        operation (str): The operation to perform (sum, avg, min, max).
        values (list): A list of numeric values.
        
    Returns:
        float: The result of the calculation.
        
    Raises:
        ValueError: If the operation is invalid or values is not a list of numbers.
    """
    if not isinstance(values, list):
        raise ValueError("Values must be a list")
    
    if not values:
        raise ValueError("Values list cannot be empty")
        
    if not all(isinstance(val, (int, float)) for val in values):
        raise ValueError("All values must be numbers")
    
    if operation == "sum":
        return sum(values)
    elif operation == "avg":
        return sum(values) / len(values)
    elif operation == "min":
        return min(values)
    elif operation == "max":
        return max(values)
    else:
        raise ValueError(f"Unsupported operation: {operation}. "
                         f"Supported operations are: sum, avg, min, max")