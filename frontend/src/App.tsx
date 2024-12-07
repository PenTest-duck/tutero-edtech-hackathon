import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Index from "./pages/Index";
// import Settings from "./pages/Settings";
import { FocusTimerProvider } from "./context/FocusTimerContext";
import { RestTimerProvider } from "./context/RestTimerContext";

function App() {
  return (
    <FocusTimerProvider>
      <RestTimerProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Index />} />
            {/* <Route path="/settings" element={<Settings />} /> */}
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </BrowserRouter>
      </RestTimerProvider>
    </FocusTimerProvider>
  );
}

export default App;
