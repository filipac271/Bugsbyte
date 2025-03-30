/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class', // Habilita o modo escuro baseado numa classe
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        "primary-100": "#0CCD73",
        "secondary-100": "#7BD8AD",
        "secondary-50": "#A3E6C7",
        "gray-100": "#010F63",
        "gray-50": "#F0F0EB"
      },
      fontFamily: {
        montserrat: ["Montserrat", "san-serif"],
      },
    },
  },
  screens: {
    xs: "480px",
    sm: "768px",
    md: "1060px",
  },
  plugins: [],
}