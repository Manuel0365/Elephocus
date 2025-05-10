import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  FlatList,
  SafeAreaView,
  TouchableOpacity,
  Modal,
  TextInput,
  Alert,
} from "react-native";
import BottomNavBar from "../../components/BottomNavBar";
import Swipeable from "react-native-gesture-handler/Swipeable";
import Icon from "react-native-vector-icons/MaterialCommunityIcons";
import * as Animatable from "react-native-animatable";
import CatalogueFlashcardsViewModel from "../../viewmodels/CatalogueFlashcardsViewModel";
import styles from "../../styles/CatalogueFlashcardsStyles";

const CatalogueFlashcardsScreen = ({ route, navigation }) => {
  const [flashcards, setFlashcards] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [flashcardEdit, setFlashcardEdit] = useState(null);
  const { temaSeleccionado } = route.params || {};

  useEffect(() => {
    CatalogueFlashcardsViewModel.cargarFlashcards(
      temaSeleccionado,
      setFlashcards
    );
  }, [temaSeleccionado]);

  const eliminarFlashcard = (id) => {
    Alert.alert(
      "Eliminar Flashcard",
      "¿Estás seguro de que deseas eliminar esta flashcard?",
      [
        { text: "Cancelar" },
        {
          text: "Eliminar",
          onPress: () =>
            CatalogueFlashcardsViewModel.eliminarFlashcard(
              id,
              flashcards,
              setFlashcards
            ),
        },
      ]
    );
  };

  const editarFlashcard = (flashcard) => {
    setFlashcardEdit(flashcard);
    setModalVisible(true);
  };

  const handleSaveEdit = () => {
    CatalogueFlashcardsViewModel.guardarFlashcardEditada(
      flashcardEdit,
      flashcards,
      setFlashcards
    );
    setModalVisible(false);
  };

  const renderItem = ({ item }) => (
    <Swipeable
      renderLeftActions={() => (
        <Animatable.View style={[styles.swipeAction, styles.deleteAction]}>
          <Icon name="delete" size={30} color="white" />
        </Animatable.View>
      )}
      renderRightActions={() => (
        <Animatable.View style={[styles.swipeAction, styles.editAction]}>
          <Icon name="pencil" size={30} color="white" />
        </Animatable.View>
      )}
      onSwipeableLeftOpen={() => eliminarFlashcard(item.id)}
      onSwipeableRightOpen={() => editarFlashcard(item)}
    >
      <TouchableOpacity style={styles.flashcardItem}>
        <Text style={styles.pregunta}>{item.pregunta}</Text>
        <Text style={styles.respuesta}>{item.respuesta}</Text>
      </TouchableOpacity>
    </Swipeable>
  );

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.titulo}>
          {temaSeleccionado
            ? `Flashcards de ${temaSeleccionado}`
            : "Catálogo de Flashcards"}
        </Text>
        <FlatList
          data={flashcards}
          renderItem={renderItem}
          keyExtractor={(item) => item.id.toString()}
          contentContainerStyle={styles.listContentContainer}
        />
        {temaSeleccionado && (
          <TouchableOpacity
            style={styles.addFlashcardButton} // Nuevo estilo
            onPress={() =>
              navigation.navigate("CrearFlashcard", {
                tema: temaSeleccionado,
              })
            }
          >
            <Text style={styles.addFlashcardButtonText}>
              Agregar Flashcard a {temaSeleccionado}
            </Text>
          </TouchableOpacity>
        )}
      </View>

      <BottomNavBar
        onHomePress={() => navigation.navigate("Main")}
        onBookPress={() => navigation.navigate("CatalogoFlashcards")}
        onAddPress={() => navigation.navigate("CrearFlashcard")}
        onListPress={() => navigation.navigate("CatalogoTemario")}
        onSettingsPress={() => navigation.navigate("Settings")}
        navigation={navigation}
      />
    </SafeAreaView>
  );
};

export default CatalogueFlashcardsScreen;