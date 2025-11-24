from flask import Flask, request, jsonify
from flask_cors import CORS
from src.services.llm_service import process_food_query


app = Flask(__name__)
CORS(app)  # 允许所有跨域请求

@app.route('/')
def root():
    return jsonify({"message": "AI饮食助手后端服务正在运行(Flask版)"})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get("query", "").lower()
    location = data.get("location", "")
    preferences = data.get("dietary_preferences", "")
    # 处理用户查询
    result = process_food_query(
        query=query,
        location=location,
        dietary_preferences=preferences
    )
    response = result['response']

    return jsonify({
        "response": response,
        "calorie_info": [],
        "recommendations": []
    })

@app.route('/api/calories/<food_name>', methods=['GET'])
def get_food_calories(food_name):
    return jsonify([
        {"name": food_name, "calories": 100, "protein": 10, "fat": 5, "carbs": 15, "note": "示例数据"}
    ])

@app.route('/api/recommendations/<location>', methods=['GET'])
def get_local_recommendations(location):
    return jsonify([
        {
            "name": f"{location}特色菜",
            "description": f"这是{location}的特色美食",
            "features": ["特色", "美食"],
            "recommended_restaurant": "当地知名餐厅",
            "calories": 300
        }
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)