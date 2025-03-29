import { useMode } from "../components/context/ModeContext";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const { mode } = useMode();
  const navigate = useNavigate();

  const handleSearch = () => {
    navigate(`/${mode}`); // Redireciona para /cliente ou /empresa
  };

  return (
    <div className="flex flex-col items-center mt-10">
      <h2 className="text-2xl font-semibold mb-4">Bem-vindo!</h2>
      <button onClick={handleSearch} className="bg-green-500 px-6 py-3 rounded">
        Pesquisar
      </button>
    </div>
  );
};

export default Home;
