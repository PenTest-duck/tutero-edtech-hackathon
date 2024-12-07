import React, { useState, useEffect } from "react";
import { Button } from "./ui/button";
import { useFocusTimer } from "../context/FocusTimerContext";
import { useRestTimer } from "../context/RestTimerContext";

const StudyTimer = () => {
  const [time, setTime] = useState(1500); // 25 minutes in seconds
  const { isActive: isFocusActive, setIsActive: setIsFocusActive } = useFocusTimer();
  const { isRestActive, setIsRestActive } = useRestTimer();
  const [isFocusMode, setIsFocusMode] = useState(true);

  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    if (isFocusActive || isRestActive) {
      interval = setInterval(() => {
        setTime((time) => (time > 0 ? time - 1 : 0));
      }, 1000);
    } else if ((!isFocusActive && time !== 0) || (!isRestActive && time !== 0)) {
      clearInterval(interval!);
    }
    return () => clearInterval(interval!);
  }, [isFocusActive, isRestActive, time]);

  useEffect(() => {
    if (time === 0) {
      if (isFocusMode) {
        setIsFocusActive(false);
        setIsFocusMode(false);
        setTime(300); // 5 minutes in seconds
      } else {
        setIsRestActive(false);
        setIsFocusMode(true);
        setTime(1500); // 25 minutes in seconds
      }
    }
  }, [time, isFocusMode, setIsFocusActive, setIsRestActive]);

  const formatTime = (seconds: number) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes < 10 ? "0" : ""}${minutes}:${remainingSeconds < 10 ? "0" : ""}${remainingSeconds}`;
  };

  const handleStartStopClick = () => {
    if (isFocusMode) {
      if (isFocusActive) {
        setIsFocusActive(false);
        setTime(1500);
      } else {
        setIsFocusActive(true);
      }
    } else {
      if (isRestActive) {
        setIsRestActive(false);
        setTime(300);
      } else {
        setIsRestActive(true);
      }
    }
  };

  return (
    <div className="bg-card text-card-foreground rounded-lg shadow-lg p-4">
      <h2 className="text-xl font-semibold mb-4">{isFocusMode ? "Focus Timer" : "Rest Timer"}</h2>
      <div className="text-4xl font-bold text-center">{formatTime(time)}</div>
      <div className="mt-4 flex justify-center space-x-2">
        <Button onClick={handleStartStopClick}>
          {isFocusMode ? (isFocusActive ? "Reset" : "Start Focus") : isRestActive ? "Reset" : "Start Break"}
        </Button>
      </div>
    </div>
  );
};

export default StudyTimer;
