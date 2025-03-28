import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const useFetchData = () => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Função para buscar os dados do CSV
  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/dados`);
      setData(response.data);
    } catch (err) {
      setError("Erro ao buscar os dados.");
    } finally {
      setLoading(false);
    }
  };

  // Função para rodar o scraper e atualizar os dados
  const runScraper = async () => {
    setLoading(true);
    try {
      await axios.post(`${API_URL}/scrape`);
      await fetchData(); // Atualiza os dados após o scraping
    } catch (err) {
      setError("Erro ao rodar o scraper.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return { data, loading, error, runScraper };
};
