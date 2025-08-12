import React from 'react';
import './Categories.css'; // Assuming you have a CSS file for styling

const Categories = () => {
  const categories = [
    { name: 'دهان', emoji: '🎨' },
    { name: 'نجارة', emoji: '🔨' },
    { name: 'كهرباء', emoji: '⚡' },
    { name: 'سباكة', emoji: '🔧' }
  ];

  return (
    <div className="categories">
      {categories.map((cat, index) => (
        <div key={index} className="category-card">
          <span className="emoji">{cat.emoji}</span>
          <p>{cat.name}</p>
        </div>
      ))}
    </div>
  );
};

export default Categories;
