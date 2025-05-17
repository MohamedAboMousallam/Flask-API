import json
import pytest
from app import create_app


@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app({'TESTING': True})
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_home_endpoint(client):
    """Test the home endpoint returns the expected response."""
    response = client.get('/')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['message'] == 'Welcome to Flask Sample App!'
    assert data['status'] == 'success'


def test_status_endpoint(client):
    """Test the status endpoint returns the expected response."""
    response = client.get('/api/v1/status')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['status'] == 'operational'
    assert 'version' in data


def test_users_endpoint(client):
    """Test the users endpoint returns the expected response."""
    response = client.get('/api/v1/users')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'users' in data
    assert 'count' in data
    assert isinstance(data['users'], list)
    assert len(data['users']) == data['count']


def test_calculate_endpoint_sum(client):
    """Test the calculate endpoint with sum operation."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'sum', 'values': [1, 2, 3, 4, 5]}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['result'] == 15


def test_calculate_endpoint_avg(client):
    """Test the calculate endpoint with avg operation."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'avg', 'values': [1, 2, 3, 4, 5]}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['result'] == 3


def test_calculate_endpoint_min(client):
    """Test the calculate endpoint with min operation."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'min', 'values': [1, 2, 3, 4, 5]}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['result'] == 1


def test_calculate_endpoint_max(client):
    """Test the calculate endpoint with max operation."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'max', 'values': [1, 2, 3, 4, 5]}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['result'] == 5


def test_calculate_endpoint_invalid_operation(client):
    """Test the calculate endpoint with an invalid operation."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'invalid', 'values': [1, 2, 3, 4, 5]}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert 'error' in data


def test_calculate_endpoint_invalid_values(client):
    """Test the calculate endpoint with invalid values."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'sum', 'values': [1, 2, "three", 4, 5]}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert 'error' in data


def test_calculate_endpoint_empty_values(client):
    """Test the calculate endpoint with empty values."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'sum', 'values': []}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert 'error' in data


def test_calculate_endpoint_missing_fields(client):
    """Test the calculate endpoint with missing required fields."""
    response = client.post(
        '/api/v1/calculate',
        data=json.dumps({'operation': 'sum'}),
        content_type='application/json'
    )
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert 'error' in data


def test_not_found(client):
    """Test that a 404 error returns the expected response."""
    response = client.get('/nonexistent')
    data = json.loads(response.data)
    
    assert response.status_code == 404
    assert 'error' in data