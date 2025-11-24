const API_BASE_URL = 'http://localhost:8080/api';

// 发送饮食查询请求
export const sendFoodQuery = async (query, location = null, dietaryPreferences = null) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        query,
        location,
        dietary_preferences: dietaryPreferences
      }),
    });

    if (!response.ok) {
      throw new Error(`API请求失败: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('发送查询请求时出错:', error);
    throw error;
  }
};

// 获取食物卡路里信息
export const getFoodCalories = async (foodName) => {
  try {
    const response = await fetch(`${API_BASE_URL}/calories/${encodeURIComponent(foodName)}`);
    
    if (!response.ok) {
      throw new Error(`获取卡路里信息失败: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('获取卡路里信息时出错:', error);
    throw error;
  }
};

// 获取当地美食推荐
export const getLocalRecommendations = async (location) => {
  try {
    const response = await fetch(`${API_BASE_URL}/recommendations/${encodeURIComponent(location)}`);
    
    if (!response.ok) {
      throw new Error(`获取美食推荐失败: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('获取美食推荐时出错:', error);
    throw error;
  }
};