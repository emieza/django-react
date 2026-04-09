const API_URL = 'http://localhost:8000/api/llibres'; // Ajusta según tu Django API

export const getBooks = () => {
  console.log('cridant API...');
  return fetch(API_URL)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error l'obtenir els llibres");
      }
      return response.json();
    })
    .catch((error) => {
      console.error('Error en la API:', error);
      return [];
    });
};
