import AsyncStorage from "@react-native-async-storage/async-storage";

const CatalogueFlashcardsViewModel = {
  cargarFlashcards: async (temaSeleccionado, setFlashcards) => {
    try {
      const flashcardsGuardadas = await AsyncStorage.getItem("flashcards");
      const todasLasFlashcards = flashcardsGuardadas
        ? JSON.parse(flashcardsGuardadas)
        : [];

      const flashcardsFiltradas = temaSeleccionado
        ? todasLasFlashcards.filter((flashcard) => flashcard.tema === temaSeleccionado)
        : todasLasFlashcards;

      setFlashcards(flashcardsFiltradas);
    } catch (error) {
      console.error("Error al cargar las flashcards:", error);
    }
  },

  eliminarFlashcard: async (id, flashcards, setFlashcards) => {
    const nuevasFlashcards = flashcards.filter(
      (flashcard) => flashcard.id !== id
    );
    await AsyncStorage.setItem("flashcards", JSON.stringify(nuevasFlashcards));
    setFlashcards(nuevasFlashcards);
  },

  guardarFlashcardEditada: async (flashcardEdit, flashcards, setFlashcards) => {
    const flashcardsActualizadas = flashcards.map((flashcard) =>
      flashcard.id === flashcardEdit.id ? flashcardEdit : flashcard
    );
    await AsyncStorage.setItem(
      "flashcards",
      JSON.stringify(flashcardsActualizadas)
    );
    setFlashcards(flashcardsActualizadas);
  },
};

export default CatalogueFlashcardsViewModel;