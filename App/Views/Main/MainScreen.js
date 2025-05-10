import React from "react";
import { View, FlatList } from "react-native";
import { useFonts } from "expo-font";
import BottomNavBar from "../../components/BottomNavBar";
import Flashcard from "../../components/Flashcard";
import RoundedImage from '../../components/RoundedImage';
import useMainScreenViewModel from "../../viewmodels/MainScreenViewModel";
import styles from "../../styles/MainScreenStyles";

const MainScreen = ({ navigation }) => {
  const { flashcards } = useMainScreenViewModel();
  const [fontsLoaded] = useFonts({
    "Oleo Script": require("../../assets/fonts/OleoScript-Regular.ttf"),
    "Oleo Script Bold": require("../../assets/fonts/OleoScript-Bold.ttf"),
  });

  if (!fontsLoaded) {
    return null;
  }

  const renderFlashcard = ({ item }) => (
    <View style={styles.cardWrapper}>
      <Flashcard pregunta={item.pregunta} respuesta={item.respuesta} />
    </View>
  );

  return (
    <View style={styles.container}>
      <RoundedImage source={require('../../assets/library.jpeg')} style={styles.topImage} />

      <View style={styles.cardsContainer}>
        {flashcards.length > 0 ? (
          <FlatList
            data={flashcards}
            renderItem={renderFlashcard}
            keyExtractor={(item, index) => index.toString()}
            horizontal
            pagingEnabled
            showsHorizontalScrollIndicator={false}
            contentContainerStyle={styles.flatListContent}
          />
        ) : (
          <View style={styles.emptyContainer}>
            <Flashcard
              pregunta="No hay flashcards disponibles"
              respuesta="Crea nuevas flashcards para comenzar"
            />
          </View>
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
    </View>
  );
};

export default MainScreen;