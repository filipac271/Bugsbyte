/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        "primary-100": "#7ED957",
        "secondary-100": "#D2F2C4",
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