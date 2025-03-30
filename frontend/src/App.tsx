import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ModeProvider } from "./components/context/ModeContext";
import Navbar from "./components/navbar";
import Home from "./pages/Home";
import Footer from "./components/footer";

function App() {
  return (
    <ModeProvider>
      <Router>
        {/* Contêiner principal com layout flex */}
        <div className="min-h-screen flex flex-col">
          <Navbar />
          <main className="flex-grow">
            <Routes>
              <Route path="/" element={<Home />} />
            </Routes>
          </main>
          {/* Footer vai ficar no final da página */}
          <Footer />
        </div>
      </Router>
    </ModeProvider>
  );
}

export default App;
