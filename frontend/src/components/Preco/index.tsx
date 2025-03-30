import { useState, useEffect } from "react";
import { novopreco, unidades, bundledesconto } from "../../api";

type Props = {
  termo: string;
  setIsOpen: (value: boolean) => void; // Adicionado para fechar o pop-up
};

const NovoPreco = ({ termo, setIsOpen }: Props) => {
  const [resultado, setResultado] = useState<{ preco: string } | null>(null);
  const [unidade, setUnidade] = useState<{ unidade: string } | null>(null);
  // const [bundledesc, setBundledesc] = useState<{ bundledesc: string } | null>(null);
  const [loading, setLoading] = useState(false);

  const buscarNovoPreco = async (termo: string) => {
    if (termo.length > 1) {
      setLoading(true);
      try {
        const preconew = await novopreco(termo);
        const uni = await unidades(termo);
        const bundle = await bundledesconto(termo);
        setResultado({ preco: preconew.toString() });
        setUnidade({ unidade: uni.toString() });
        // setBundledesc({ bundledesc: bundle.toString() });
      } catch (error) {
        console.error("Erro ao buscar novo preço:", error);
      }
      setLoading(false);
    } else {
      setResultado(null);
      setUnidade(null);
      // setBundledesc(null);
    }
  };

  useEffect(() => {
    buscarNovoPreco(termo);
  }, [termo]);

  return (
    <div className="bg-white dark:bg-slate-800 p-6 rounded-lg shadow-lg w-1/3 text-center">
      <h2 className="text-2xl font-bold text-center mb-2 dark:text-white">
        O preço sugerido é...
      </h2>

      {/* Exibe o preço com a unidade, se ambos estiverem disponíveis */}
      <strong className="text-3xl dark:text-white">
        {loading
          ? "Carregando..."
          : resultado?.preco && unidade?.unidade
          ? `${resultado.preco} ${unidade.unidade}`
          : "Sem dados"}
      </strong>
      {/* <p className="text-3xl dark:text-white">
        {loading
          ? "Carregando..."
          : bundledesc?.bundledesc
          ? `${bundledesc.bundledesc}`
          : "Sem dados"}
      </p> */}

      <p className="mt-2 dark:text-white">
        Este valor é calculado através dos dados sazonais, isto é, quando um
        produto é mais popular, e altera o preço baseado nessa demanda.
      </p>
      <button
        onClick={() => setIsOpen(false)} // Agora fecha corretamente
        className="mt-4 px-4 py-2 bg-primary-100 text-black rounded-md hover:bg-secondary-50"
      >
        Fechar
      </button>
    </div>
  );
};

export default NovoPreco;
