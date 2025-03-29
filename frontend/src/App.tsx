
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ModeProvider } from "./components/context/ModeContext";
import Navbar from "./components/navbar";
import Home from "./pages/Home";
import Cliente from "./pages/Cliente";
import Empresa from "./pages/Empresa";


function App() {

  return (

    <ModeProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cliente" element={<Cliente />} />
          <Route path="/empresa" element={<Empresa />} />
        </Routes>
      </Router>
    </ModeProvider>

  );
}

export default App;
