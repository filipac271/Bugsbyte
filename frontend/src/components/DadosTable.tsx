import React from "react";
import { useFetchData } from "../hooks/useFetchData";

const DadosTable: React.FC = () => {
  const { data, loading, error, runScraper } = useFetchData();

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Dados do CSV</h2>

      {/* Botão para rodar o Scraper */}
      <button
        onClick={runScraper}
        className="bg-blue-500 text-white px-4 py-2 rounded-lg mb-4 hover:bg-blue-600 transition"
        disabled={loading}
      >
        {loading ? "Carregando..." : "Atualizar Dados (Scraper)"}
      </button>

      {/* Exibir erros, se houver */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Tabela de Dados */}
      <div className="overflow-x-auto">
        <table className="table-auto border-collapse border border-gray-300 w-full">
          <thead>
            <tr className="bg-gray-200">
              {Object.keys(data[0] || {}).map((key) => (
                <th key={key} className="border border-gray-300 px-4 py-2">{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index} className="hover:bg-gray-100">
                {Object.values(item).map((value, i) => (
                  <td key={i} className="border border-gray-300 px-4 py-2">{value}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DadosTable;
