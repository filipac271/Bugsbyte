import React, { useState } from "react";
import Search from "../Search";
import NovoPreco from "../Preco";

const Home = () => {
  const [texto, setTexto] = useState<string>("");
  const [isOpen, setIsOpen] = useState<boolean>(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setTexto(e.target.value);
  };

  return (
    <div className="justify-center ">
      <div className="flex flex-row justify-center items-center">
        <img src="./euro.png" className="mt-[74px]" width="400" alt="Euro" />
      </div>

      {/* Campo de pesquisa */}
      <div className="flex justify-center">
        <div className="flex justify-center mt-[40px]">
          <input
            type="text"
            value={texto}
            onChange={handleChange}
            className="bg-primary-100 px-[20px] py-[15px] rounded-full text-left text-black placeholder:text-black w-[400px] h-[50px]" // Definir altura explícita
            placeholder="Pesquise pelo produto pretendido"
          />
        </div>
        <div className="flex justify-center mt-[40px] ml-4">
          <button
            onClick={() => setIsOpen(true)}
            className="py-[15px] px-[20px] bg-primary-100 rounded-full h-[50px] flex items-center justify-center" // Definir altura e garantir alinhamento
          >
            Sugestão de preço
          </button>
        </div>
      </div>

      {/* Passar o valor do termo para o Search */}
      <div className="flex dark:bg-slate-800 justify-center mt-[40px] pb-7">
        <Search termo={texto} />
      </div>
    {/**Botao do pop up */}
      {isOpen && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
          <NovoPreco termo={texto} setIsOpen={setIsOpen} />
        </div>
      )}
    </div>
  );
};

export default Home;
