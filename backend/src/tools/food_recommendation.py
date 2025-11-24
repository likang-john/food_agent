from typing import List, Dict, Any
import requests

def get_local_food_recommendations(location: str) -> List[Dict[str, Any]]:
    """
    根据用户位置获取当地特色美食推荐
    
    Args:
        location: 用户所在位置（城市或地区）
    
    Returns:
        推荐美食列表，每个元素包含美食名称、描述和特点
    """
    # 在实际应用中，这里应该调用外部API或查询数据库
    # 现在使用内置的美食推荐数据库进行模拟
    
    # 内置的城市美食推荐数据库（示例）
    food_recommendations_db = {
        "北京": [
            {
                "name": "北京烤鸭",
                "description": "北京最著名的特色菜，皮脆肉嫩",
                "features": ["传统名菜", "宫廷风味", "历史悠久"],
                "recommended_restaurant": "全聚德",
                "calories": "约400大卡/100克"
            },
            {
                "name": "炸酱面",
                "description": "老北京传统面食，酱香浓郁",
                "features": ["家常面食", "酱香浓郁", "爽口开胃"],
                "recommended_restaurant": "老北京炸酱面馆",
                "calories": "约350大卡/100克"
            },
            {
                "name": "豆汁焦圈",
                "description": "地道的北京小吃，风味独特",
                "features": ["传统小吃", "风味独特", "历史悠久"],
                "recommended_restaurant": "护国寺小吃",
                "calories": "约200大卡/份"
            },
            {
                "name": "涮羊肉",
                "description": "冬季暖身的首选，鲜美多汁",
                "features": ["冬季美食", "鲜香可口", "社交聚餐"],
                "recommended_restaurant": "东来顺",
                "calories": "约280大卡/100克"
            }
        ],
        "上海": [
            {
                "name": "小笼包",
                "description": "上海特色点心，皮薄馅多汤汁鲜美",
                "features": ["传统点心", "皮薄馅多", "汤汁鲜美"],
                "recommended_restaurant": "南翔馒头店",
                "calories": "约200大卡/4个"
            },
            {
                "name": "生煎包",
                "description": "底部金黄酥脆，肉馅鲜嫩",
                "features": ["街头美食", "外酥里嫩", "鲜香可口"],
                "recommended_restaurant": "小杨生煎",
                "calories": "约250大卡/4个"
            },
            {
                "name": "红烧肉",
                "description": "上海本帮菜代表作，肥而不腻",
                "features": ["本帮名菜", "甜而不腻", "色泽红亮"],
                "recommended_restaurant": "上海老饭店",
                "calories": "约330大卡/100克"
            }
        ],
        "广州": [
            {
                "name": "广式早茶",
                "description": "丰富多样的点心组合，包括虾饺、烧卖等",
                "features": ["饮食文化", "种类丰富", "精致可口"],
                "recommended_restaurant": "陶陶居",
                "calories": "约500-800大卡/套"
            },
            {
                "name": "白切鸡",
                "description": "广东名菜，肉质嫩滑，原汁原味",
                "features": ["粤菜经典", "肉质嫩滑", "原汁原味"],
                "recommended_restaurant": "广州酒家",
                "calories": "约200大卡/100克"
            },
            {
                "name": "煲仔饭",
                "description": "用瓦煲烹制的米饭，香气四溢",
                "features": ["传统美食", "香气四溢", "口感丰富"],
                "recommended_restaurant": "陈添记煲仔饭",
                "calories": "约350大卡/份"
            }
        ],
        "成都": [
            {
                "name": "火锅",
                "description": "四川特色，麻辣鲜香",
                "features": ["川菜代表", "麻辣鲜香", "社交聚餐"],
                "recommended_restaurant": "小龙坎",
                "calories": "约300-500大卡/100克"
            },
            {
                "name": "麻婆豆腐",
                "description": "经典川菜，麻辣鲜香，豆腐嫩滑",
                "features": ["川菜经典", "麻辣鲜香", "豆腐嫩滑"],
                "recommended_restaurant": "陈麻婆豆腐",
                "calories": "约180大卡/100克"
            },
            {
                "name": "串串香",
                "description": "将各种食材串在竹签上烫煮",
                "features": ["街头小吃", "麻辣可口", "自选食材"],
                "recommended_restaurant": "钢管厂五区小郡肝",
                "calories": "约250大卡/100克"
            }
        ],
        "西安": [
            {
                "name": "肉夹馍",
                "description": "陕西特色小吃，馍香肉嫩",
                "features": ["传统小吃", "馍香肉嫩", "方便快捷"],
                "recommended_restaurant": "老潼关肉夹馍",
                "calories": "约350大卡/个"
            },
            {
                "name": "凉皮",
                "description": "夏季消暑小吃，清爽可口",
                "features": ["夏季美食", "清爽可口", "酸辣开胃"],
                "recommended_restaurant": "魏家凉皮",
                "calories": "约200大卡/份"
            },
            {
                "name": "羊肉泡馍",
                "description": "陕西名吃，汤鲜肉烂",
                "features": ["传统名菜", "营养丰富", "暖身开胃"],
                "recommended_restaurant": "同盛祥",
                "calories": "约400大卡/份"
            }
        ]
    }
    
    # 转换为小写进行匹配
    location_lower = location.lower()
    
    # 精确匹配城市
    for city in food_recommendations_db:
        if location == city or location_lower == city.lower():
            return food_recommendations_db[city]
    
    # 模糊匹配城市名
    for city in food_recommendations_db:
        if location_lower in city.lower() or city.lower() in location_lower:
            return food_recommendations_db[city]
    
    # 如果没有找到特定城市的推荐，返回通用推荐
    return [
        {
            "name": "当地特色菜",
            "description": f"{location}地区有丰富的美食文化，建议尝试当地特色餐厅",
            "features": ["当地特色", "文化体验", "新鲜食材"],
            "recommended_restaurant": "当地知名餐厅",
            "calories": "因菜品而异"
        },
        {
            "name": "健康沙拉",
            "description": "新鲜蔬果制作的健康选择",
            "features": ["健康营养", "低热量", "清爽开胃"],
            "recommended_restaurant": "当地沙拉店",
            "calories": "约150-250大卡/份"
        },
        {
            "name": "当地面食",
            "description": f"{location}地区的特色面食",
            "features": ["传统美食", "饱腹耐饿", "风味独特"],
            "recommended_restaurant": "当地面食馆",
            "calories": "约300-400大卡/份"
        }
    ]

def get_dietary_preference_recommendations(dietary_preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    根据用户的饮食偏好提供推荐
    
    Args:
        dietary_preferences: 饮食偏好，如素食、低卡路里、高蛋白等
    
    Returns:
        符合饮食偏好的推荐食物列表
    """
    # 基础推荐数据库
    all_recommendations = [
        {
            "name": "蔬菜沙拉",
            "description": "新鲜蔬菜混合橄榄油和柠檬汁",
            "dietary_tags": ["vegetarian", "low_calorie", "low_fat"],
            "calories": "约180大卡/份",
            "protein": "5克",
            "fat": "15克",
            "carbs": "7克"
        },
        {
            "name": "鸡胸肉炒蔬菜",
            "description": "嫩煎鸡胸肉配各种时令蔬菜",
            "dietary_tags": ["high_protein", "low_carbs"],
            "calories": "约250大卡/份",
            "protein": "30克",
            "fat": "10克",
            "carbs": "8克"
        },
        {
            "name": "清蒸鱼",
            "description": "新鲜鱼肉清蒸，保留原汁原味",
            "dietary_tags": ["high_protein", "low_fat"],
            "calories": "约180大卡/份",
            "protein": "25克",
            "fat": "5克",
            "carbs": "0克"
        },
        {
            "name": "素食炒饭",
            "description": "各种蔬菜丁炒米饭，营养均衡",
            "dietary_tags": ["vegetarian"],
            "calories": "约350大卡/份",
            "protein": "10克",
            "fat": "10克",
            "carbs": "55克"
        },
        {
            "name": "水果沙拉",
            "description": "多种时令水果混合",
            "dietary_tags": ["vegetarian", "low_fat", "low_calorie"],
            "calories": "约150大卡/份",
            "protein": "2克",
            "fat": "0克",
            "carbs": "35克"
        },
        {
            "name": "糙米饭配豆腐",
            "description": "糙米和嫩煎豆腐的健康组合",
            "dietary_tags": ["vegetarian", "high_fiber"],
            "calories": "约300大卡/份",
            "protein": "12克",
            "fat": "8克",
            "carbs": "45克"
        }
    ]
    
    # 根据饮食偏好筛选推荐
    filtered_recommendations = []
    
    for food in all_recommendations:
        tags = food["dietary_tags"]
        match = True
        
        # 检查素食偏好
        if dietary_preferences.get("vegetarian") and "vegetarian" not in tags:
            match = False
        
        # 检查低卡路里偏好
        if dietary_preferences.get("low_calorie") and "low_calorie" not in tags:
            match = False
        
        # 检查高蛋白偏好
        if dietary_preferences.get("high_protein") and "high_protein" not in tags:
            match = False
        
        # 检查低碳水偏好
        if dietary_preferences.get("low_carbs") and "low_carbs" not in tags:
            match = False
        
        if match:
            filtered_recommendations.append(food)
    
    return filtered_recommendations