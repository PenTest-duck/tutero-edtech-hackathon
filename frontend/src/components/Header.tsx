import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header className="bg-primary text-primary-foreground shadow-md">
      <div className="container mx-auto px-4 py-6 flex justify-between items-center">
        <h1 className="text-2xl font-bold">StudyBuddy AI</h1>
        <nav>
          <ul className="flex space-x-4">
            {/* <li>
              <Link to="/" className="hover:underline">
                Home
              </Link>
            </li> */}
            {/* <li>
              <Link to="/settings" className="hover:underline">
                Settings
              </Link>
            </li> */}
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
