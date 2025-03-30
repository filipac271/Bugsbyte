import { useDarkMode } from "../hooks/useDarkMode";

const DarkModeToggle = () => {
  const { isDarkMode, toggleDarkMode } = useDarkMode();

  return (
    <button
      onClick={toggleDarkMode}
      className="p-2 px-3 py-2 rounded-full hover:bg-green-500 font-semibold bg-primary-100 dark:bg-slate-800 text-gray-800 dark:text-gray-200 transition-all"
    >
      {isDarkMode ? "🌙" : "☀️"}
    </button>
  );
};

export default DarkModeToggle;
