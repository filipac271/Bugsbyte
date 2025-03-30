
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ModeProvider } from "./components/context/ModeContext";
import Navbar from "./components/navbar";
import Home from "./pages/Home";



function App() {

  return (

    <ModeProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </Router>
    </ModeProvider>

  );
}

export default App;
