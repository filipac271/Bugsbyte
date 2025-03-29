import React, { useState } from 'react';
import logo from './logo.svg';
import Navbar from './components/navbar';
import Footer from './components/footer'
import euro from './components/images/euro.png'

function App() {
  const [texto, setTexto] = useState<string>("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setTexto(e.target.value);
  };

  return (
    <div className="App">
      <Navbar />
      <div className="justify-center flex-items-center">
        <div className="flex flex-center justify-center items-center">
          <img src={euro} className="mt-[120px]" width="300" alt="Euro" />
        </div>
        <div className="flex justify-center mt-[40px]">
         <input
          type="text"
          value={texto}
          onChange={handleChange}
          className="bg-primary-100 px-[20px] py-[15px] rounded-full text-left text-black placeholder:text-black w-[400px]" // A classe placeholder:text-black altera a cor do placeholder
          placeholder="Pesquisa pelo produto pretendido"
         />
        </div>



        
        {/* Caixa de texto */}
        <div className="text-center mt-5">
          
        </div>

        {/* Mostrar o texto digitado */}
        <div className="text-center mt-5">
          <h2>Você digitou: {texto}</h2>
        </div>
      </div>

      {/* <Footer/> */}
    </div>
  );
}

export default App;
