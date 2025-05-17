import pytest
from app.utils import calculate_result


def test_calculate_result_sum():
    """Test calculate_result with sum operation."""
    result = calculate_result('sum', [1, 2, 3, 4, 5])
    assert result == 15


def test_calculate_result_avg():
    """Test calculate_result with avg operation."""
    result = calculate_result('avg', [1, 2, 3, 4, 5])
    assert result == 3


def test_calculate_result_min():
    """Test calculate_result with min operation."""
    result = calculate_result('min', [1, 2, 3, 4, 5])
    assert result == 1


def test_calculate_result_max():
    """Test calculate_result with max operation."""
    result = calculate_result('max', [1, 2, 3, 4, 5])
    assert result == 5


def test_calculate_result_invalid_operation():
    """Test calculate_result with invalid operation."""
    with pytest.raises(ValueError) as excinfo:
        calculate_result('invalid', [1, 2, 3, 4, 5])
    assert "Unsupported operation" in str(excinfo.value)


def test_calculate_result_not_a_list():
    """Test calculate_result with non-list values."""
    with pytest.raises(ValueError) as excinfo:
        calculate_result('sum', "not a list")
    assert "Values must be a list" in str(excinfo.value)


def test_calculate_result_empty_list():
    """Test calculate_result with empty list."""
    with pytest.raises(ValueError) as excinfo:
        calculate_result('sum', [])
    assert "Values list cannot be empty" in str(excinfo.value)


def test_calculate_result_non_numeric_values():
    """Test calculate_result with non-numeric values."""
    with pytest.raises(ValueError) as excinfo:
        calculate_result('sum', [1, 2, "three", 4, 5])
    assert "All values must be numbers" in str(excinfo.value)