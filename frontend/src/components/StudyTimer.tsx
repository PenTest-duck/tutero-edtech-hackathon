import React, { useState, useEffect } from "react";
import { Button } from "./ui/button";
import { useTimer } from "../context/TimerContext";

const StudyTimer = () => {
  const [time, setTime] = useState(1500); // 25 minutes in seconds
  const { isActive, setIsActive } = useTimer();

  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    if (isActive) {
      interval = setInterval(() => {
        setTime((time) => (time > 0 ? time - 1 : 0));
      }, 1000);
    } else if (!isActive && time !== 0) {
      clearInterval(interval!);
    }
    return () => clearInterval(interval!);
  }, [isActive, time]);

  const formatTime = (seconds: number) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes < 10 ? "0" : ""}${minutes}:${remainingSeconds < 10 ? "0" : ""}${remainingSeconds}`;
  };

  const handleStart = () => {
    setIsActive(true);
  };

  const handleReset = () => {
    setIsActive(false);
    setTime(1500);
  };

  const handleStartStopClick = () => {
    if (isActive) {
      handleReset();
    } else {
      handleStart();
    }
  };

  return (
    <div className="bg-card text-card-foreground rounded-lg shadow-lg p-4">
      <h2 className="text-xl font-semibold mb-4">Study Timer</h2>
      <div className="text-4xl font-bold text-center">{formatTime(time)}</div>
      <div className="mt-4 flex justify-center space-x-2">
        <Button onClick={handleStartStopClick}>{isActive ? "Reset" : "Start"} </Button>
        {/* <Button variant="outline" onClick={handleReset}>
          Reset
        </Button> */}
      </div>
    </div>
  );
};

export default StudyTimer;
