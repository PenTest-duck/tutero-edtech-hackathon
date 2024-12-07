import React, { createContext, useState, useContext, ReactNode } from "react";

interface RestTimerContextProps {
  isRestActive: boolean;
  setIsRestActive: React.Dispatch<React.SetStateAction<boolean>>;
}

const RestTimerContext = createContext<RestTimerContextProps | undefined>(undefined);

export const RestTimerProvider = ({ children }: { children: ReactNode }) => {
  const [isRestActive, setIsRestActive] = useState(false);

  return <RestTimerContext.Provider value={{ isRestActive, setIsRestActive }}>{children}</RestTimerContext.Provider>;
};

export const useRestTimer = () => {
  const context = useContext(RestTimerContext);
  if (!context) {
    throw new Error("useRestTimer must be used within a RestTimerProvider");
  }
  return context;
};
