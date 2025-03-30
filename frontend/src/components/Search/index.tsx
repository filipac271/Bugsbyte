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
      <div className="w-[1000px] mx-2">
      {termo.length > 0 && (
        <div className="flex justify-between bg-primary-100 border rounded-md font-bold">
        <div className="text-left w-2/5 pl-2">Produto</div>
        <div className="text-center w-1/4">Preço</div>
        <div className="text-right w-1/4 pr-2">Supermercado</div>
      </div>
      )}
  
    <ul className="bg-secondary-100 border rounded-md shadow-md">
      {resultados.map((item, index) => (
        <div
          key={index}
          className="flex justify-between border-b hover:bg-secondary-50 cursor-pointer"
    >
        <div className="text-left w-2/5 pl-2"><strong>{item.Produtos}</strong></div>
        <div className="text-center w-1/4">{item.preco || item.Preco}</div>
        <div className="text-right w-1/4 pr-2">{item.loja || item.Loja}</div>
      </div>
    ))}
    </ul>
      </div>



    </div>
  );
};

export default Search;
