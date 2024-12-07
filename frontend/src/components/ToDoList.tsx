import React, { useState, useEffect } from "react";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { getLocalStorage, setLocalStorage } from "@/scripts/store";
import { FaEllipsisV } from "react-icons/fa";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

interface Task {
  id: number;
  text: string;
  completed: boolean;
}

const ToDoList = () => {
  const [tasks, setTasks] = useState<Task[]>(() => getLocalStorage("tasks"));
  const [newTask, setNewTask] = useState("");
  const [editingTaskId, setEditingTaskId] = useState<number | null>(null);
  const [editingTaskText, setEditingTaskText] = useState("");
  const [openDropdownId, setOpenDropdownId] = useState<number | null>(null);

  useEffect(() => {
    setLocalStorage("tasks", tasks);
  }, [tasks]);

  const handleAddTask = () => {
    if (newTask.trim() === "") return;
    const newTaskObj: Task = {
      id: Date.now(),
      text: newTask,
      completed: false,
    };
    setTasks([...tasks, newTaskObj]);
    setNewTask("");
  };

  const handleToggleTask = (id: number) => {
    setTasks(tasks.map((task) => (task.id === id ? { ...task, completed: !task.completed } : task)));
  };

  const handleDeleteTask = (id: number) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  const handleEditTask = (id: number, text: string) => {
    setEditingTaskId(id);
    setEditingTaskText(text);
  };

  const handleSaveEdit = () => {
    setTasks(tasks.map((task) => (task.id === editingTaskId ? { ...task, text: editingTaskText } : task)));
    setEditingTaskId(null);
    setEditingTaskText("");
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleAddTask();
    }
  };

  return (
    <div className="bg-card text-card-foreground rounded-lg shadow-lg p-4">
      <h2 className="text-xl font-semibold mb-4">To-Do List</h2>
      <div className="space-y-2">
        <div className="flex items-center space-x-2">
          <Input
            type="text"
            placeholder="Add a task"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            onKeyPress={handleKeyPress}
          />
          <Button onClick={handleAddTask}>Add</Button>
        </div>
        <ul className="mt-2 space-y-1">
          {tasks.map((task) => (
            <li key={task.id} className="flex justify-between items-center space-x-2 group">
              <div className="flex items-center space-x-2">
                <input
                  type="checkbox"
                  checked={task.completed}
                  onChange={() => handleToggleTask(task.id)}
                  className="rounded text-primary focus:ring-primary"
                />
                {editingTaskId === task.id ? (
                  <input
                    type="text"
                    value={editingTaskText}
                    onChange={(e) => setEditingTaskText(e.target.value)}
                    onBlur={handleSaveEdit}
                    onKeyPress={(e) => e.key === "Enter" && handleSaveEdit()}
                    className="border rounded px-2 py-1"
                  />
                ) : (
                  <span className={task.completed ? "line-through" : ""}>{task.text}</span>
                )}
              </div>
              <div className="relative">
                <DropdownMenu onOpenChange={(open) => setOpenDropdownId(open ? task.id : null)}>
                  <DropdownMenuTrigger className="focus:outline-none">
                    <FaEllipsisV
                      className={`transition-opacity ${
                        openDropdownId === task.id ? "opacity-100" : "opacity-0 group-hover:opacity-100"
                      }`}
                    />
                  </DropdownMenuTrigger>
                  <DropdownMenuContent>
                    <DropdownMenuItem onClick={() => handleEditTask(task.id, task.text)}>Edit</DropdownMenuItem>
                    <DropdownMenuItem onClick={() => handleDeleteTask(task.id)}>Delete</DropdownMenuItem>
                  </DropdownMenuContent>
                </DropdownMenu>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ToDoList;
