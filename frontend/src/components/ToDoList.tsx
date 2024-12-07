import React from "react";
import { Button } from "./ui/button";
import { Input } from "./ui/input";

const ToDoList = () => {
  return (
    <div className="bg-card text-card-foreground rounded-lg shadow-lg p-4">
      <h2 className="text-xl font-semibold mb-4">To-Do List</h2>
      <div className="space-y-2">
        <div className="flex items-center space-x-2">
          <Input type="text" placeholder="Add a task" />
          <Button>Add</Button>
        </div>
        <ul className="mt-2 space-y-1">
          <li className="flex items-center space-x-2">
            <input type="checkbox" className="rounded text-primary focus:ring-primary" />
            <span>Complete math homework</span>
          </li>
          <li className="flex items-center space-x-2">
            <input type="checkbox" className="rounded text-primary focus:ring-primary" />
            <span>Read chapter 5 of history book</span>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default ToDoList;
