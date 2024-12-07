import React from "react";
import { Button } from "./ui/button";

const StudyTimer = () => {
  return (
    <div className="bg-card text-card-foreground rounded-lg shadow-lg p-4">
      <h2 className="text-xl font-semibold mb-4">Study Timer</h2>
      <div className="text-4xl font-bold text-center">25:00</div>
      <div className="mt-4 flex justify-center space-x-2">
        <Button>Start</Button>
        <Button variant="outline">Reset</Button>
      </div>
    </div>
  );
};

export default StudyTimer;
