
import config from '../config';

const API_BASE_URL = config.API_URL;
export const IMAGE_SRC = config.MEDIA_URL;

export const getBooks = () => {
  console.log('cridant API...');
  return fetch(API_BASE_URL+'/llibres')
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error a l'obtenir els llibres");
      }
      return response.json();
    })
    .catch((error) => {
      console.error('Error en la API:', error);
      return [];
    });
};

export const getBookDetails = (id) => {
  console.log('cridant API details book id='+id);
  return fetch(API_BASE_URL+'/llibre/'+id)
    .then((response) => {
      console.log(response);
      return response;
    })
    .catch((error) => {
      console.error('Error en la API:', error);
      return [];
    });
};

