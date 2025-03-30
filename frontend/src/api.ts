import axios, { AxiosInstance } from "axios";

const API_URL = "http://localhost:8080";
console.log("API URL: ", API_URL); // Add this line to check if the URL is set correctly

export const API: AxiosInstance = axios.create({
  baseURL: API_URL,
  responseType: "json",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function search(termo: string) {
  const res = API.get(`/search?q=${termo}`);
  console.log("response: ", res); // Log the response to see if it's redirected to the wrong port
  return res;
}

export async function novopreco(termo:string) {
  const preco = await API.get(`/novopreco?q=${termo}`);
  console.log("preco:", preco);
  return preco.data;
}

export async function unidades (termo:string){
  const uni = await API.get(`/unidades?q=${termo}`);
  console.log("unidade:", uni);
  return uni.data;
}

export async function bundledesconto(termo:string) {
  const bundle= await API.get(`/bundledesconto?q=${termo}`);
  console.log("bundles:", bundle);
  return bundle.data;
}