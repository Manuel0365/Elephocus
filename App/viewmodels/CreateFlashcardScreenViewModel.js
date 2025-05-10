import { useState } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";

const useCreateFlashcardScreenViewModel = () => {
  const [pregunta, setPregunta] = useState("");
  const [respuesta, setRespuesta] = useState("");

  const handleGuardarFlashcard = async () => {
    const nuevaFlashcard = { pregunta, respuesta };
    try {
      const flashcardsGuardadas = await AsyncStorage.getItem("flashcards");
      const flashcards = flashcardsGuardadas ? JSON.parse(flashcardsGuardadas) : [];
      flashcards.push(nuevaFlashcard);
      await AsyncStorage.setItem("flashcards", JSON.stringify(flashcards));
      console.log("Flashcard guardada correctamente");
      setPregunta("");
      setRespuesta("");
    } catch (error) {
      console.error("Error al guardar la flashcard:", error);
    }
  };

  return { pregunta, respuesta, setPregunta, setRespuesta, handleGuardarFlashcard };
};

export default useCreateFlashcardScreenViewModel;