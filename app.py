from flask import Flask, request, jsonify, send_from_directory
import re
import math
import os

app = Flask(__name__)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Clean the expression
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        
        # Validate expression - only allow numbers, operators, parentheses, and decimal points
        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return jsonify({'error': 'Invalid expression'}), 400
        
        # Evaluate the expression safely
        result = eval(expression)
        
        # Handle special cases
        if math.isnan(result) or math.isinf(result):
            return jsonify({'error': 'Math error'}), 400
        
        # Round to avoid floating point precision issues
        if isinstance(result, float):
            result = round(result, 10)
            # Remove trailing zeros
            if result == int(result):
                result = int(result)
        
        return jsonify({'result': str(result)})
    
    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero'}), 400
    except Exception as e:
        return jsonify({'error': 'Invalid expression'}), 400

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)