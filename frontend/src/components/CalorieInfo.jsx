import React from 'react';

const CalorieInfo = ({ calories }) => {
  // 格式化营养信息显示
  const formatNutritionInfo = (info) => {
    if (typeof info === 'object' && info !== null) {
      return (
        <div className="nutrition-details">
          <p>热量: {info.calories} 大卡{(info.note ? ` (${info.note})` : '')}</p>
          {info.protein !== undefined && <p>蛋白质: {info.protein} 克</p>}
          {info.fat !== undefined && <p>脂肪: {info.fat} 克</p>}
          {info.carbs !== undefined && <p>碳水化合物: {info.carbs} 克</p>}
        </div>
      );
    }
    return <p>{info}</p>;
  };

  return (
    <div className="calorie-info">
      <h4>营养信息</h4>
      <div className="calorie-list">
        {Array.isArray(calories) && calories.map((foodItem, index) => (
          <div key={index} className="food-calorie-item">
            <div className="food-name">{foodItem.name}</div>
            {formatNutritionInfo(foodItem)}
          </div>
        ))}
      </div>
    </div>
  );
};

export default CalorieInfo;