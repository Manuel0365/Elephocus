import { useState, useEffect } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";

// Función para obtener flashcards desde AsyncStorage
const obtenerFlashcards = async () => {
  try {
    const flashcardsGuardadas = await AsyncStorage.getItem("flashcards");
    return flashcardsGuardadas ? JSON.parse(flashcardsGuardadas) : [];
  } catch (error) {
    console.error("Error al obtener las flashcards:", error);
    return [];
  }
};

const useMainScreenViewModel = () => {
  const [flashcards, setFlashcards] = useState([]);

  useEffect(() => {
    const cargarFlashcards = async () => {
      const flashcardsGuardadas = await obtenerFlashcards();
      setFlashcards(flashcardsGuardadas);
    };
    cargarFlashcards();
  }, []);

  return { flashcards };
};

export default useMainScreenViewModel;
