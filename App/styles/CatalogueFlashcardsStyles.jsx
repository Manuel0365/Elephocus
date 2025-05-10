import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F7F7F7",
  },
  content: {
    flex: 1,
    paddingHorizontal: 20,
    paddingTop: 30,
  },
  titulo: {
    fontSize: 26,
    fontWeight: "700",
    color: "#4A148C",
    marginBottom: 20,
    textAlign: "center",
  },
  flashcardItem: {
    backgroundColor: "#9f8b9f",
    padding: 20,
    marginVertical: 12,
    borderRadius: 15,
    elevation: 6,
  },
  pregunta: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#FFFFFF",
    textAlign: "center",
    marginBottom: 10,
  },
  respuesta: {
    fontSize: 16,
    color: "#F5F5F5",
    textAlign: "center",
  },
  swipeAction: {
    justifyContent: "center",
    alignItems: "center",
    width: 75,
    height: 75,
    borderRadius: 50,
  },
  deleteAction: {
    backgroundColor: "rgba(255, 0, 0, 0.8)",
  },
  editAction: {
    backgroundColor: "rgba(200, 100, 255, 0.8)",
  },
  listContentContainer: {
    paddingBottom: 100,
  },
  addFlashcardButton: { // Estilos para el botón
    backgroundColor: "#4A148C",
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 20,
    elevation: 3,
  },
  addFlashcardButtonText: {
    color: "white",
    fontSize: 16,
    fontWeight: "bold",
  },
});

export default styles;