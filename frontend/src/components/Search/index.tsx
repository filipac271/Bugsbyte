import { useState, useEffect } from "react";
import { API, search } from "../../api";

interface SearchProps {
  termo: string; // Recebendo o termo de busca como prop
}

const Search = ({ termo }: SearchProps) => {
  const [resultados, setResultados] = useState<
    {
      Produtos?: string;
      Produto?: string;
      preco?: string;
      Preco?: string;
      loja?: string;
      Loja?: string;
    }[]
  >([]);

  const [loading, setLoading] = useState(false);

  // Função para buscar os dados na API
  const buscarDados = async (termo: string) => {
    if (termo.length > 1) {
      setLoading(true);
      const res = await search(termo);

      // Normaliza os nomes das chaves
      const dadosFormatados = res.data.map((item: any) => ({
        Produtos: item.Produtos || "Desconhecido",
        preco: item.Preco || "Preço indisponível",
        loja: item.Loja || "Loja desconhecida",
      }));

      setResultados(dadosFormatados);
      setLoading(false);
    } else {
      setResultados([]);
    }
  };

  // Usando useEffect para buscar os dados sempre que o termo mudar
  useEffect(() => {
    buscarDados(termo);
  }, [termo]);

  return (
    <div>
      {/* Indicador de carregamento */}
      {loading && <p>Carregando...</p>}

      {/* Resultados da pesquisa */}
      <ul className="mt-4 border rounded-md shadow-md">
        {resultados.map((item, index) => (
          <li
            key={index}
            className="p-2 border-b hover:bg-gray-100 cursor-pointer"
          >
            <strong>{item.Produtos}</strong> - {item.preco || item.Preco} -{" "}
            {item.loja || item.Loja}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Search;
