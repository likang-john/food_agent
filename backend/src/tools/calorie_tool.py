from typing import Dict, Any, Optional
import json
import os

def get_calorie_info(food_name: str) -> Dict[str, Any]:
    """
    获取食物的卡路里和营养信息
    
    Args:
        food_name: 食物名称
    
    Returns:
        包含卡路里和营养信息的字典
    """
    # 在实际应用中，这里应该调用外部API或查询数据库
    # 现在使用内置的食物数据库进行模拟
    
    # 内置的食物卡路里数据库（示例）
    calorie_database = {
        "米饭": {
            "calories": 116,
            "protein": 2.6,
            "fat": 0.3,
            "carbs": 25.9,
            "portion": "100克"
        },
        "面条": {
            "calories": 138,
            "protein": 5.5,
            "fat": 0.7,
            "carbs": 25.0,
            "portion": "100克"
        },
        "鸡肉": {
            "calories": 165,
            "protein": 31.0,
            "fat": 3.6,
            "carbs": 0,
            "portion": "100克生鸡肉"
        },
        "牛肉": {
            "calories": 250,
            "protein": 26.0,
            "fat": 17.0,
            "carbs": 0,
            "portion": "100克生牛肉"
        },
        "鱼肉": {
            "calories": 124,
            "protein": 20.4,
            "fat": 4.0,
            "carbs": 0,
            "portion": "100克生鱼"
        },
        "蔬菜": {
            "calories": 25,
            "protein": 1.5,
            "fat": 0.3,
            "carbs": 5.0,
            "portion": "100克"
        },
        "水果": {
            "calories": 52,
            "protein": 0.3,
            "fat": 0.2,
            "carbs": 13.8,
            "portion": "100克"
        },
        "宫保鸡丁": {
            "calories": 190,
            "protein": 16.0,
            "fat": 10.0,
            "carbs": 10.0,
            "portion": "100克"
        },
        "清蒸鲈鱼": {
            "calories": 105,
            "protein": 20.0,
            "fat": 2.2,
            "carbs": 0,
            "portion": "100克"
        },
        "西红柿炒蛋": {
            "calories": 130,
            "protein": 8.0,
            "fat": 10.0,
            "carbs": 3.0,
            "portion": "100克"
        },
        "沙拉": {
            "calories": 180,
            "protein": 5.0,
            "fat": 15.0,
            "carbs": 7.0,
            "portion": "100克"
        },
        "汉堡": {
            "calories": 254,
            "protein": 12.0,
            "fat": 10.0,
            "carbs": 30.0,
            "portion": "100克"
        },
        "披萨": {
            "calories": 266,
            "protein": 11.0,
            "fat": 10.0,
            "carbs": 33.0,
            "portion": "100克"
        }
    }
    
    # 转换为小写进行匹配
    food_name_lower = food_name.lower()
    
    # 精确匹配
    if food_name in calorie_database:
        return calorie_database[food_name]
    
    # 模糊匹配
    for key in calorie_database:
        if food_name_lower in key.lower() or key.lower() in food_name_lower:
            return calorie_database[key]
    
    # 按关键词匹配
    keywords = {
        "米": "米饭",
        "面": "面条",
        "鸡": "鸡肉",
        "牛": "牛肉",
        "鱼": "鱼肉",
        "菜": "蔬菜",
        "果": "水果"
    }
    
    for keyword, food_key in keywords.items():
        if keyword in food_name:
            return calorie_database[food_key]
    
    # 如果没有找到，返回通用信息
    return {
        "calories": "未知",
        "protein": "未知",
        "fat": "未知",
        "carbs": "未知",
        "portion": "100克",
        "note": "未找到该食物的详细信息"
    }

def calculate_total_calories(food_items: list) -> Dict[str, Any]:
    """
    计算多个食物的总卡路里和营养成分
    
    Args:
        food_items: 食物项目列表，每个项目包含食物名称和重量
    
    Returns:
        包含总营养信息的字典
    """
    total_calories = 0
    total_protein = 0
    total_fat = 0
    total_carbs = 0
    detailed_info = {}
    
    for item in food_items:
        food_name = item.get("name", "")
        weight = item.get("weight", 100)  # 默认100克
        
        try:
            calorie_info = get_calorie_info(food_name)
            
            # 计算实际重量的营养成分
            if calorie_info["calories"] != "未知":
                calories = calorie_info["calories"] * weight / 100
                protein = calorie_info["protein"] * weight / 100
                fat = calorie_info["fat"] * weight / 100
                carbs = calorie_info["carbs"] * weight / 100
                
                total_calories += calories
                total_protein += protein
                total_fat += fat
                total_carbs += carbs
                
                detailed_info[food_name] = {
                    "calories": round(calories, 1),
                    "protein": round(protein, 1),
                    "fat": round(fat, 1),
                    "carbs": round(carbs, 1),
                    "weight": weight
                }
        except Exception as e:
            detailed_info[food_name] = {"error": str(e)}
    
    return {
        "total_calories": round(total_calories, 1),
        "total_protein": round(total_protein, 1),
        "total_fat": round(total_fat, 1),
        "total_carbs": round(total_carbs, 1),
        "detailed_info": detailed_info
    }