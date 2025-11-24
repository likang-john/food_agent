import React, { useState } from 'react';

const Navbar = ({ onLocationChange, onPreferencesChange, dietaryPreferences }) => {
  const [showPreferences, setShowPreferences] = useState(false);
  const [location, setLocation] = useState('');
  const [tempPreferences, setTempPreferences] = useState(dietaryPreferences || {});

  // 处理位置输入变化
  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  // 保存位置
  const handleSaveLocation = () => {
    if (location.trim()) {
      onLocationChange(location.trim());
    }
  };

  // 处理饮食偏好变化
  const handlePreferenceChange = (key) => {
    setTempPreferences(prev => ({
      ...prev,
      [key]: !prev[key]
    }));
  };

  // 保存饮食偏好
  const handleSavePreferences = () => {
    onPreferencesChange(tempPreferences);
    setShowPreferences(false);
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <h1>🍽️ AI饮食助手</h1>
      </div>
      
      <div className="navbar-controls">
        <div className="location-input-group">
          <input
            type="text"
            placeholder="输入您的位置（可选）"
            value={location}
            onChange={handleLocationChange}
            className="location-input"
          />
          <button onClick={handleSaveLocation} className="save-location-btn">
            保存位置
          </button>
        </div>
        
        <div className="preferences-control">
          <button 
            onClick={() => setShowPreferences(!showPreferences)}
            className="preferences-btn"
          >
            饮食偏好
          </button>
          
          {showPreferences && (
            <div className="preferences-dropdown">
              <h4>选择您的饮食偏好</h4>
              <div className="preference-options">
                <label className="preference-option">
                  <input
                    type="checkbox"
                    checked={tempPreferences.vegetarian || false}
                    onChange={() => handlePreferenceChange('vegetarian')}
                  />
                  素食
                </label>
                <label className="preference-option">
                  <input
                    type="checkbox"
                    checked={tempPreferences.low_calorie || false}
                    onChange={() => handlePreferenceChange('low_calorie')}
                  />
                  低卡路里
                </label>
                <label className="preference-option">
                  <input
                    type="checkbox"
                    checked={tempPreferences.high_protein || false}
                    onChange={() => handlePreferenceChange('high_protein')}
                  />
                  高蛋白
                </label>
                <label className="preference-option">
                  <input
                    type="checkbox"
                    checked={tempPreferences.low_carbs || false}
                    onChange={() => handlePreferenceChange('low_carbs')}
                  />
                  低碳水
                </label>
              </div>
              <button onClick={handleSavePreferences} className="save-preferences-btn">
                保存偏好
              </button>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;