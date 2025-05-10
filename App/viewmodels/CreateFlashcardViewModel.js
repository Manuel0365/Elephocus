import { useState } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { useCatalogoTemarioViewModel } from "./CatalogoTemarioViewModel";

const useCreateFlashcardViewModel = () => {
  const [pregunta, setPregunta] = useState("");
  const [respuesta, setRespuesta] = useState("");
  const catalogoTemarioViewModel = useCatalogoTemarioViewModel();
  const [tema, setTema] = useState(catalogoTemarioViewModel.temas[0] || ""); // Inicializa con el primer tema o cadena vacía

  const handleGuardarFlashcard = async () => {
    if (!pregunta.trim() || !respuesta.trim() || !tema) {
      Alert.alert("Error", "Por favor, completa todos los campos.");
      return;
    }

    const nuevaFlashcard = { pregunta, respuesta, tema, id: Date.now().toString() }; // Asegúrate de tener un ID único
    try {
      const flashcardsGuardadas = await AsyncStorage.getItem("flashcards");
      const flashcards = flashcardsGuardadas ? JSON.parse(flashcardsGuardadas) : [];
      flashcards.push(nuevaFlashcard);
      await AsyncStorage.setItem("flashcards", JSON.stringify(flashcards));
      console.log("Flashcard guardada correctamente");
      setPregunta("");
      setRespuesta("");
      setTema(catalogoTemarioViewModel.temas[0] || "");
    } catch (error) {
      console.error("Error al guardar la flashcard:", error);
      Alert.alert("Error", "Hubo un error al guardar la flashcard.");
    }
  };

  return {
    pregunta,
    respuesta,
    tema,
    setPregunta,
    setRespuesta,
    setTema,
    handleGuardarFlashcard,
  };
};

export default useCreateFlashcardViewModel;