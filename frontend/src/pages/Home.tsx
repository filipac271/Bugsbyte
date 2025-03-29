import { useMode } from "../components/context/ModeContext";
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import euro from './euro.png';
import Search from "../components/Search"; // Importando o componente de busca

const Home = () => {
  const { mode } = useMode(); // Usando o contexto para definir o modo (cliente ou empresa)
  const navigate = useNavigate();
  const [texto, setTexto] = useState<string>("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setTexto(e.target.value); // Atualizando o texto da busca
  };

  const handleSearch = () => {
    navigate(`/${mode}`); // Redireciona com base no modo selecionado
  };

  return (
    <div className="justify-center flex-items-center">
      <div className="flex flex-center justify-center items-center">
        <img src='./euro.png' className="mt-[120px]" width="300" alt="Euro" />
      </div>

      {/* Campo de pesquisa aqui */}
      <div className="flex justify-center mt-[40px]">
        <input
          type="text"
          value={texto}
          onChange={handleChange} // Atualizando o estado com a digitação do usuário
          className="bg-primary-100 px-[20px] py-[15px] rounded-full text-left text-black placeholder:text-black w-[400px]"
          placeholder="Pesquisa pelo produto pretendido"
        />
      </div>

      {/* Passando o valor do termo para o Search */}
      <div className="flex justify-center mt-[40px]">
        <Search termo={texto} />
      </div>

      <div className="text-center mt-5"></div>

      {/* Mostrar o texto digitado */}
      <div className="text-center mt-5">
        <h2>Você digitou: {texto}</h2>
      </div>
    </div>
  );
};

export default Home;
