from flask import Flask, request, jsonify
import numpy as np
import re

app = Flask(__name__)

@app.route('/compute', methods=['POST'])
def compute():
    try:
        data = request.get_json()
        expression = data.get('expression', '')

        # 验证表达式，仅允许数字和基本运算符
        if not re.match(r'^[\d+\-*/. ()np.sqrt]+$', expression):
            return jsonify({'error': 'Invalid expression'}), 400

        # 计算表达式结果
        try:
            result = eval(expression, {'np': np})
        except Exception as e:
            return jsonify({'error': str(e)}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/')
def home():
    return "Flask server is running!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
