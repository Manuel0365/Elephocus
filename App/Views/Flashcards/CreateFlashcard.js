import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Platform, // Mantén Platform aquí
} from "react-native";
import { Picker } from "@react-native-picker/picker"; // Importa Picker desde la librería correcta
import BottomNavBar from "../../components/BottomNavBar";
import useCreateFlashcardViewModel from "../../viewmodels/CreateFlashcardViewModel";
import { useCatalogoTemarioViewModel } from "../../viewmodels/CatalogoTemarioViewModel";
import styles from "../../styles/CreateFlashcardStyles";

const CrearFlashcardScreen = ({ navigation, route }) => {
  const {
    pregunta,
    respuesta,
    tema,
    setPregunta,
    setRespuesta,
    setTema,
    handleGuardarFlashcard,
  } = useCreateFlashcardViewModel();
  const catalogoTemarioViewModel = useCatalogoTemarioViewModel();
  const [temas, setTemas] = useState([]);

  useEffect(() => {
    catalogoTemarioViewModel.cargarTemas();
    setTemas(catalogoTemarioViewModel.temas);

    // Si se pasa un tema desde la pantalla de catálogo, seleccionarlo por defecto
    if (route.params?.tema) {
      setTema(route.params.tema);
    }
  }, [route.params?.tema]);

  return (
    <View style={styles.container}>
      <View style={styles.content}>
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
        {Platform.OS === "ios" ? (
          <Picker
            selectedValue={tema}
            style={styles.input}
            onValueChange={(itemValue) => setTema(itemValue)}
          >
            {temas.map((t, index) => (
              <Picker.Item key={index} label={t} value={t} />
            ))}
          </Picker>
        ) : (
          <Picker
            selectedValue={tema}
            style={styles.input}
            onValueChange={(itemValue) => setTema(itemValue)}
          >
            {temas.map((t, index) => (
              <Picker.Item key={index} label={t} value={t} />
            ))}
          </Picker>
        )}
        <TouchableOpacity
          style={styles.botonGuardar}
          onPress={handleGuardarFlashcard}
        >
          <Text style={styles.botonGuardarTexto}>Guardar</Text>
        </TouchableOpacity>
      </View>
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