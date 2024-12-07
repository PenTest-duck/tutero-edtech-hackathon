import React, { createContext, useState, useContext, ReactNode } from "react";

interface FocusTimerContextProps {
  isActive: boolean;
  setIsActive: React.Dispatch<React.SetStateAction<boolean>>;
}

const FocusTimerContext = createContext<FocusTimerContextProps | undefined>(undefined);

export const FocusTimerProvider = ({ children }: { children: ReactNode }) => {
  const [isActive, setIsActive] = useState(false);

  return <FocusTimerContext.Provider value={{ isActive, setIsActive }}>{children}</FocusTimerContext.Provider>;
};

export const useFocusTimer = () => {
  const context = useContext(FocusTimerContext);
  if (!context) {
    throw new Error("useFocusTimer must be used within a FocusTimerProvider");
  }
  return context;
};
