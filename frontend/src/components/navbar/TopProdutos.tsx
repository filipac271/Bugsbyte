import React from "react";
import { useState, useEffect } from "react";

const produtos = [
  {
    name: "Citrinos do Algarve IGP Laranja 70/95Kg",
  },
  {
    name: "Banana CAT I Continente KG",
  },
  {
    name: "Morango embalagem 500Gr",
  },
  {
    name: "Açucar Branco Continente 1Kg",
  },
  {
    name: "Peito de Frango 2Kg",
  },
  {
    name: "Compal/AT",
  },
];

type Props = {
  setIsOpen: (value: boolean) => void; // Adicionado para fechar o pop-up
};

const TopProdutos = ({setIsOpen}: Props) => {
  return (
    <div className="bg-white dark:bg-slate-800 p-6 rounded-lg shadow-lg w-1/3 text-center">
      <h2 className="text-2xl font-bold text-center mb-2 dark:text-white">
        Os Produtos mais vendidos são:
      </h2>
      {produtos.map((produto) => (
        <div key={produto.name}>
          <div className=" text-xl dark:text-white">{produto.name}</div>
        </div>
      ))}{" "}
      <button
        onClick={() => setIsOpen(false)} // Agora fecha corretamente
        className="mt-4 px-4 py-2 bg-primary-100 text-black rounded-md hover:bg-secondary-50"
      >
        Fechar
      </button>
    </div>
  );
};

export default TopProdutos;
