import React from "react";
import { View, Text, TextInput, Button } from "react-native";
import useCreateFlashcardScreenViewModel from "../../viewmodels/CreateFlashcardScreenViewModel";
import styles from "../../styles/CreateFlashcardScreenStyles";
import BottomNavBar from "../../components/BottomNavBar";

const CrearFlashcardScreen = ({navigation}) => {
  const {
    pregunta,
    respuesta,
    setPregunta,
    setRespuesta,
    handleGuardarFlashcard,
  } = useCreateFlashcardScreenViewModel();

  return (
    <View style={styles.container}>
      <Text style={styles.titulo}>Crear Flashcard</Text>
      <TextInput
        style={styles.input}
        placeholder="Pregunta"
        value={pregunta}
        onChangeText={setPregunta}
      />
      <TextInput
        style={styles.input}
        placeholder="Respuesta"
        value={respuesta}
        onChangeText={setRespuesta}
      />
      <Button title="Guardar" onPress={handleGuardarFlashcard} />
      <BottomNavBar
        onHomePress={() => navigation.navigate("Main")}
        onBookPress={() => navigation.navigate("CatalogoFlashcards")}
        onAddPress={() => navigation.navigate("CrearFlashcard")}
        onListPress={() => navigation.navigate("CatalogoTemario")}
        onSettingsPress={() => navigation.navigate("Settings")}
        navigation={navigation}
      />
    </View>
  );
};

export default CrearFlashcardScreen;