import { useMode } from "../components/context/ModeContext";
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import Search from "../components/Search"; 

const Home = () => {
  const { mode } = useMode(); 
  const navigate = useNavigate();
  const [texto, setTexto] = useState<string>("");
  const [isOpen, setIsOpen] = useState<boolean>(false); 

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setTexto(e.target.value);
  };

  const handleSearch = () => {
    navigate(`/${mode}`); // Redireciona com base no modo selecionado
  };

  return (
    <div className="justify-center bg-gray-50 min-h-screen">
      <div className="flex flex-row justify-center items-center">
        <img src='./euro.png' className="mt-[120px]" width="300" alt="Euro" />
      </div>

      {/* Campo de pesquisa */}
      <div className="flex justify-center">
       <div className="flex justify-center mt-[40px]">
        <input
         type="text"
         value={texto}
         onChange={handleChange}
         className="bg-primary-100 px-[20px] py-[15px] rounded-full text-left text-black placeholder:text-black w-[400px] h-[50px]" // Definir altura explícita
         placeholder="Pesquisa pelo produto pretendido"
        />
      </div>
      <div className="flex justify-center mt-[40px] ml-4">
        <button
         onClick={() => setIsOpen(true)}
         className="py-[15px] px-[20px] bg-primary-100 rounded-full h-[50px] flex items-center justify-center" // Definir altura e garantir alinhamento
        >
         Abrir Pop-up
        </button>
       </div>
      </div>


      {/* Passando o valor do termo para o Search */}
      <div className="flex justify-center mt-[40px]">
        <Search termo={texto} />
      </div>

      {/* Botão para abrir o pop-up */}


      {/* Pop-up (modal) */}
      {isOpen && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-1/3">
            <h2 className="text-xl font-bold">Este é um Pop-up!</h2>
            <p className="mt-2">Aqui podes adicionar qualquer conteúdo.</p>
            
            {/* Botão para fechar */}
            <button
              onClick={() => setIsOpen(false)}
              className="mt-4 px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600"
            >
              Fechar
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;
