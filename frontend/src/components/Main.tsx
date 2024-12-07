import React from "react";
import WebcamFeed from "./WebcamFeed";
import StudyBuddyMessages from "./StudyBuddyMessages";
import StudyTimer from "./StudyTimer";
import ToDoList from "./ToDoList";

const Main = () => {
  return (
    <main className="flex-grow container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="md:col-span-2 space-y-8">
          <WebcamFeed />
          <StudyBuddyMessages />
        </div>
        <div className="space-y-8">
          <StudyTimer />
          <ToDoList />
        </div>
      </div>
    </main>
  );
};

export default Main;
