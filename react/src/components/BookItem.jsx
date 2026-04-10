import React, { useState } from 'react';
import { IMAGE_SRC, getBookDetails } from '../services/api';

function BookItem({ book }) {
  const [modalObert, setModalObert] = useState(false);
  const [detallsLlibre, setDetallsLlibre] = useState(null);
  const [carregant, setCarregant] = useState(false);
  const [error, setError] = useState(null);

  async function mostraDetalls() {
    setModalObert(true);
    setCarregant(true);
    setError(null);
    console.log(`book id=${book.id}`)
    try {
      // Suposem que tens una API amb un endpoint per obtenir detalls d'un llibre per ID
      // Ajusta la URL segons la teva API
      //const response = await fetch(`http://localhost:8000/api/llibre/${book.id}`);
      const response = await getBookDetails(book.id);
      
      if (!response.ok) {
        throw new Error('Error carregant els detalls del llibre');
      }
      
      const data = await response.json();
      setDetallsLlibre(data);
    } catch (err) {
      setError(err.message);
      console.error('Error:', err);
    } finally {
      setCarregant(false);
    }
  }

  function tancaModal() {
    setModalObert(false);
    setDetallsLlibre(null);
    setError(null);
    setCarregant(false);
  }

  // Funció per mostrar el contingut del modal
  const renderModalContent = () => {
    if (carregant) {
      return <div className="loading">Carregant detalls...</div>;
    }
    
    if (error) {
      return <div className="error">Error: {error}</div>;
    }
    
    // Si tenim detalls de l'API, els mostrem
    if (detallsLlibre) {
      return (
        <>
          <p><strong>Autor:</strong> {detallsLlibre.autor || book.autor}</p>
          <p><strong>Data d'edició:</strong> {detallsLlibre.data_edicio || book.data_edicio || 'No disponible'}</p>
          <p><strong>Resum:</strong> {detallsLlibre.resum || book.resum || 'Sense descripció'}</p>
          
          {detallsLlibre.imatge_set.length > 0 ? (
            detallsLlibre.imatge_set.map((image) => <img height="100" src={IMAGE_SRC+image.arxiu} />)
          ) : (
            <p>Encara no hi ha imatges...</p>
          )}
        </>
      );
    }
    
    // Fallback: mostrar les dades inicials del llibre
    return (
      <>
        <p><strong>Autor:</strong> {book.autor}</p>
        <p><strong>Data d'edició:</strong> {book.data_edicio || 'No disponible'}</p>
        <p><strong>Resum:</strong> {book.resum || 'Sense descripció'}</p>
      </>
    );
  };

  return (
    <div className="book-card">
      <h3>{book.titol}</h3>
      <p>
        <strong>Autor:</strong> {book.autor}
      </p>
      <button onClick={mostraDetalls}>Detalls</button>

      {/* Modal */}
      {modalObert && (
        <div className="modal-overlay" onClick={tancaModal}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h2>{book.titol}</h2>
              <button className="close-btn" onClick={tancaModal}>×</button>
            </div>
            <div className="modal-body">
              {renderModalContent()}
            </div>
            <div className="modal-footer">
              <button onClick={tancaModal}>Tancar</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default BookItem;