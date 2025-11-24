import React, { useState, useEffect } from 'react';
import ChatInterface from '../components/ChatInterface';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { sendFoodQuery } from '../services/apiService';
import '../styles/main.css';

const MainPage = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [userLocation, setUserLocation] = useState('');
  const [dietaryPreferences, setDietaryPreferences] = useState({});

  // 发送用户消息并获取响应
  const handleSendMessage = async (query) => {
    // 添加用户消息到聊天记录
    const userMessage = {
      id: Date.now(),
      type: 'user',
      content: query
    };
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      // 调用API获取响应
      const response = await sendFoodQuery(query, userLocation, dietaryPreferences);
      
      // 添加AI响应到聊天记录
      const aiMessage = {
        id: Date.now() + 1,
        type: 'ai',
        content: response.response,
        foodItems: response.calorie_info,
        calories: response.calorie_info,
        recommendations: response.recommendations
      };
      
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      // 添加错误消息
      const errorMessage = {
        id: Date.now() + 1,
        type: 'error',
        content: '抱歉，我暂时无法回答您的问题。请稍后再试。'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  // 更新用户位置
  const handleLocationChange = (location) => {
    setUserLocation(location);
  };

  // 更新饮食偏好
  const handlePreferencesChange = (preferences) => {
    setDietaryPreferences(preferences);
  };

  return (
    <div className="main-container">
      <Navbar 
        onLocationChange={handleLocationChange}
        onPreferencesChange={handlePreferencesChange}
        dietaryPreferences={dietaryPreferences}
      />
      <main className="content">
        <ChatInterface 
          messages={messages}
          onSendMessage={handleSendMessage}
          isLoading={isLoading}
        />
      </main>
      <Footer />
    </div>
  );
};

export default MainPage;