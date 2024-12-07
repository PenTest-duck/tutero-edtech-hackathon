import React from "react";

const StudyBuddyMessages = () => {
  return (
    <div className="bg-card text-card-foreground rounded-lg shadow-lg p-4">
      <h2 className="text-xl font-semibold mb-4">Study Buddy Messages</h2>
      <div className="space-y-2">
        <p className="p-2 bg-muted rounded-md">Welcome back! Ready to start studying?</p>
        <p className="p-2 bg-muted rounded-md">Remember to stay focused on your tasks.</p>
      </div>
    </div>
  );
};

export default StudyBuddyMessages;
