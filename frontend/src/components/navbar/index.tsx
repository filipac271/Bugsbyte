import React from "react";
import { Link } from "react-router-dom";
import DarkModeToggle from "../DarkModeToggle";
import { useState, useEffect } from "react";
import TopProdutos from "./TopProdutos";

type Props = {};

const Navbar = (props: Props) => {
  const [isOpen, setIsOpen] = useState<boolean>(false);

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
            <div className="flex items-center gap-x-4">
              <button
                onClick={() => setIsOpen(true)}
                className="h-[50px] p-2 px-3 py-2 rounded-full hover:bg-green-500 font-semibold bg-primary-100 dark:bg-slate-800 text-gray-800 dark:text-gray-200"
              >
                Mais vendidos ✨
              </button>
              <DarkModeToggle />
            </div>
          </div>
        </div>
      </div>
      {isOpen && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
          <TopProdutos setIsOpen={setIsOpen} />
        </div>
      )}
    </nav>
  );
};

export default Navbar;
