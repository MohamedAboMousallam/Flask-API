from flask import jsonify, request
from app.utils import calculate_result


def register_routes(app):
    @app.route('/')
    def home():
        """Main route that returns a welcome message"""
        return jsonify({
            'message': 'Welcome to Flask Sample App!',
            'status': 'success'
        })

    @app.route('/api/v1/status')
    def status():
        """Returns the API status"""
        return jsonify({
            'status': 'operational',
            'version': '1.0.0'
        })

    @app.route('/api/v1/users')
    def users():
        """Returns a list of sample users"""
        sample_users = [
            {'id': 1, 'name': 'Alice Johnson', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob Smith', 'email': 'bob@example.com'},
            {'id': 3, 'name': 'Charlie Brown', 'email': 'charlie@example.com'}
        ]
        return jsonify({
            'users': sample_users,
            'count': len(sample_users)
        })

    @app.route('/api/v1/calculate', methods=['POST'])
    def calculate():
        """Performs a calculation based on the provided data"""
        if not request.is_json:
            return jsonify({
                'error': 'Invalid request, JSON required'
            }), 400

        data = request.get_json()
        
        if 'operation' not in data or 'values' not in data:
            return jsonify({
                'error': 'Missing required fields: operation and values'
            }), 400
            
        try:
            result = calculate_result(data['operation'], data['values'])
            return jsonify({
                'operation': data['operation'],
                'values': data['values'],
                'result': result
            })
        except ValueError as e:
            return jsonify({
                'error': str(e)
            }), 400

    @app.errorhandler(404)
    def not_found(e):
        """Handle 404 errors"""
        return jsonify({
            'error': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def server_error(e):
        """Handle 500 errors"""
        return jsonify({
            'error': 'Internal server error'
        }), 500