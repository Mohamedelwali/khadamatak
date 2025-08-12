import React from 'react';
import { FaBell, FaHeart, FaMapMarkerAlt } from 'react-icons/fa';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="nav-left">
        <span className="logo">خدماتك</span>
        <span className="tagline">منصة الخدمات الذكية</span>
      </div>
      <div className="nav-center">
        <input type="text" placeholder="بحث" className="search-input" />
      </div>
      <div className="nav-right">
        <FaBell className="icon" />
        <span className="user">rewan</span>
        <span className="role">عميل</span>
      </div>
    </nav>
  );
};

export default Navbar;
