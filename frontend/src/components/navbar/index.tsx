import React from "react";

import { useMode } from "../context/ModeContext";
import { Link } from "react-router-dom";

type Props = {};

const Navbar = (props: Props) => {
  const { mode, toggleMode } = useMode();
  const flexBetween = "flex items-center justify-between";
  return (
    <nav>
      <div
        className={`${flexBetween} sticky top-0 z-30 w-full py-5 bg-green-200 `}
      >
        <div className={`${flexBetween} mx-auto w-11/12 `}>
          {/**Lado esquerdo-> Laf tale */}
          <div className={"${flexBetween}"}>
            {/**Vai ter a imagem aqui */}
            <Link to="/">
            <img alt="logo"
            src='/laftale.jpeg'
            className="w-auto max-w-[140px] h-auto"
            />  
            </Link>  
          </div>
          {/**Lada direito o tal do botao */}
          <div className={`${flexBetween} `}>
            {/** o tal botao*/}
            <div className={``}>
              <button
                onClick={toggleMode}
                className="rounded-full bg-primary-100 px-10 py-2 hover:bg-green-500 font-semibold"
              >
                Modo: {mode === "cliente" ? "Cliente" : "Empresa"}
              </button>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
