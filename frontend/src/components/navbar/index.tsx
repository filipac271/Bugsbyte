import React from "react";

import { useMode } from "../context/ModeContext";
import { Link } from "react-router-dom";
import DarkModeToggle from "../DarkModeToggle";

type Props = {};

const Navbar = (props: Props) => {
  const { mode, toggleMode } = useMode();
  const flexBetween = "flex items-center justify-between ";
  return (
    <nav>
      <div
        className={`${flexBetween} sticky top-0 z-30 w-full py-5 bg-secondary-100 dark:bg-secondary-200`}
      >
        <div className={`${flexBetween} mx-auto w-11/12 `}>
          {/**Lado esquerdo-> Laf tale */}
          <div className={"${flexBetween}"}>
            {/**Vai ter a imagem aqui */}
            <Link to="/">
              <img
                alt="logo"
                src="/laftale.jpeg"
                className="w-auto max-w-[140px] h-auto"
              />
            </Link>
          </div>
          {/**Lada direito o tal do botao */}
          <div className={`${flexBetween} `}>
            {/** o tal botao*/}
            <div>
              <DarkModeToggle />
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
