import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  FlatList,
  SafeAreaView,
  Modal,
  TextInput,
  Button,
  Alert,
} from "react-native";
import { observer } from "mobx-react-lite";
import { useCatalogoTemarioViewModel } from "../../viewmodels/CatalogoTemarioViewModel";
import BottomNavBar from "../../components/BottomNavBar";
import styles from "../../styles/CatalogoTemarioStyles";

const CatalogoTemario = observer(({ navigation }) => {
  const catalogoTemarioViewModel = useCatalogoTemarioViewModel();
  const [modalVisible, setModalVisible] = useState(false);
  const [nuevoTema, setNuevoTema] = useState("");

  useEffect(() => {
    catalogoTemarioViewModel.cargarTemas();
  }, []);

  const handleTemaPress = (tema) => {
    navigation.navigate("CatalogoFlashcards", { temaSeleccionado: tema });
  };

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.itemContainer}
      onPress={() => handleTemaPress(item)}
    >
      <Text style={styles.itemText}>{item}</Text>
    </TouchableOpacity>
  );

  const agregarTema = () => {
    if (nuevoTema.trim()) {
      if (catalogoTemarioViewModel.temas.includes(nuevoTema.trim())) {
        Alert.alert("Error", "Este tema ya existe.");
      } else {
        catalogoTemarioViewModel.agregarTema(nuevoTema.trim());
        setNuevoTema("");
        setModalVisible(false);
      }
    } else {
      Alert.alert("Error", "El nombre del tema no puede estar vacío.");
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Temarios</Text>
        <FlatList
          data={catalogoTemarioViewModel.temas}
          renderItem={renderItem}
          keyExtractor={(item, index) => `${item}-${index}`}
        />
        <TouchableOpacity
          style={styles.addButton}
          onPress={() => setModalVisible(true)}
        >
          <Text style={styles.addButtonText}>Agregar Tema</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.bottomNavBar}>
        <BottomNavBar
          onHomePress={() => navigation.navigate("Main")}
          onBookPress={() => navigation.navigate("CatalogoFlashcards")}
          onAddPress={() => navigation.navigate("CrearFlashcard")}
          onListPress={() => navigation.navigate("CatalogoTemario")}
          onSettingsPress={() => navigation.navigate("Settings")}
          navigation={navigation}
        />
      </View>

      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <Text style={styles.modalTitle}>Agregar Nuevo Tema</Text>
            <TextInput
              style={styles.modalInput}
              placeholder="Nombre del tema"
              value={nuevoTema}
              onChangeText={setNuevoTema}
            />
            <View style={styles.modalButtonsContainer}>
              <Button title="Cancelar" onPress={() => setModalVisible(false)} color="#888" />
              <Button title="Agregar" onPress={agregarTema} color="#800080" />
            </View>
          </View>
        </View>
      </Modal>
    </SafeAreaView>
  );
});

export default CatalogoTemario;