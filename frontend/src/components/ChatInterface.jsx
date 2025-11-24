import React, { useState, useRef, useEffect } from 'react';
import MessageBubble from './MessageBubble';
import TypingIndicator from './TypingIndicator';

const ChatInterface = ({ messages, onSendMessage, isLoading }) => {
  const [inputMessage, setInputMessage] = useState('');
  const messagesEndRef = useRef(null);

  // 自动滚动到最新消息
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  // 处理发送消息
  const handleSend = (e) => {
    e.preventDefault();
    if (inputMessage.trim() && !isLoading) {
      onSendMessage(inputMessage.trim());
      setInputMessage('');
    }
  };

  return (
    <div className="chat-interface">
      <div className="chat-header">
        <h2>AI饮食助手</h2>
        <p>我可以为您推荐美食、提供食谱和卡路里信息</p>
      </div>
      
      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <p>您好！我是您的AI饮食助手。请问有什么可以帮助您的？</p>
            <p className="welcome-hint">例如："今天晚上吃什么？"、"西红柿炒蛋的做法"、"苹果的卡路里是多少？"</p>
          </div>
        ) : (
          messages.map(message => (
            <MessageBubble key={message.id} message={message} />
          ))
        )}
        
        {isLoading && <TypingIndicator />}
        <div ref={messagesEndRef} /> {/* 滚动锚点 */}
      </div>
      
      <form className="chat-input-form" onSubmit={handleSend}>
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder="请输入您的问题..."
          disabled={isLoading}
          className="chat-input"
          onKeyPress={(e) => e.key === 'Enter' && handleSend(e)}
        />
        <button 
          type="submit" 
          disabled={!inputMessage.trim() || isLoading}
          className="send-button"
        >
          发送
        </button>
      </form>
    </div>
  );
};

export default ChatInterface;