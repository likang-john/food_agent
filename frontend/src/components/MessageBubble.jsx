import React from 'react';
import CalorieInfo from './CalorieInfo';
import RecommendationsList from './RecommendationsList';

const MessageBubble = ({ message }) => {
  // 根据消息类型渲染不同样式
  const getBubbleClass = () => {
    switch (message.type) {
      case 'user':
        return 'user-bubble';
      case 'ai':
        return 'ai-bubble';
      case 'error':
        return 'error-bubble';
      default:
        return '';
    }
  };

  return (
    <div className={`message-bubble ${getBubbleClass()}`}>
      {message.type === 'user' && <div className="message-avatar">👤</div>}
      {message.type === 'ai' && <div className="message-avatar">🤖</div>}
      
      <div className="message-content">
        <p>{message.content}</p>
        
        {/* 显示卡路里信息 */}
        {message.calories && Array.isArray(message.calories) && message.calories.length > 0 && (
          <CalorieInfo calories={message.calories} />
        )}
        
        {/* 显示推荐列表 */}
        {message.recommendations && message.recommendations.length > 0 && (
          <RecommendationsList recommendations={message.recommendations} />
        )}
      </div>
    </div>
  );
};

export default MessageBubble;