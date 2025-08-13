import React from "react";
import { FaHome, FaWrench, FaUserFriends, FaCog, FaSignOutAlt } from "react-icons/fa";
import "./Sidebar.css";

const Sidebar = () => {
  return (
    <div className="sidebar" dir="rtl">
        <div>
      <div className="sidebar-logo">
        <h2>خدماتك 🔧</h2>
      </div>
      <div className="sidebar-menu">
        <div className="sidebar-item">
          <FaHome className="icon homee" />
          <span>الرئيسية</span>
        </div>
        <div className="sidebar-item">
          <FaWrench className="icon wrench" />
          <span>الخدمات</span>
        </div>
        <div className="sidebar-item">
          <FaUserFriends className="icon users" />
          <span>العملاء</span>
        </div>
        <div className="sidebar-item">
          <FaCog className="icon settings" />
          <span>الإعدادات</span>
        </div>
      </div>
      <div className="sidebar-footer">
        <div>
        <div className="sidebar-item">
          <FaSignOutAlt className="icon logout" />
          <span>تسجيل الخروج</span>
        </div>
        </div>
      </div>
      </div>
    </div>
  );
};

export default Sidebar;
