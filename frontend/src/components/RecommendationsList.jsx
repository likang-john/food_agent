import React from 'react';

const RecommendationsList = ({ recommendations }) => {
  return (
    <div className="recommendations-list">
      <h4>美食推荐</h4>
      <div className="recommendations-grid">
        {recommendations.map((item, index) => (
          <div key={index} className="recommendation-card">
            <div className="recommendation-name">{item.name}</div>
            <div className="recommendation-description">{item.description}</div>
            
            {item.features && item.features.length > 0 && (
              <div className="recommendation-features">
                {item.features.map((feature, i) => (
                  <span key={i} className="feature-tag">{feature}</span>
                ))}
              </div>
            )}
            
            {item.recommended_restaurant && (
              <div className="recommended-restaurant">
                <strong>推荐餐厅:</strong> {item.recommended_restaurant}
              </div>
            )}
            
            {item.calories && (
              <div className="recommendation-calories">
                <strong>热量:</strong> {item.calories}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecommendationsList;