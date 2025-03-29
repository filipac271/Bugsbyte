import { createContext, useContext, useState, ReactNode } from "react";

interface ModeContextProps {
  mode: "cliente" | "empresa";
  toggleMode: () => void;
}

const ModeContext = createContext<ModeContextProps | undefined>(undefined);

export const ModeProvider = ({ children }: { children: ReactNode }) => {
  const [mode, setMode] = useState<"cliente" | "empresa">("cliente");

  const toggleMode = () => {
    setMode((prev) => (prev === "cliente" ? "empresa" : "cliente"));
  };

  return (
    <ModeContext.Provider value={{ mode, toggleMode }}>
      {children}
    </ModeContext.Provider>
  );
};

export const useMode = () => {
  const context = useContext(ModeContext);
  if (!context) throw new Error("useMode must be used within a ModeProvider");
  return context;
};
