import React, { useState, useRef, useEffect } from "react";
import {
  Text,
  TouchableOpacity,
  Animated,
  StyleSheet,
  View,
} from "react-native";

const Flashcard = ({ pregunta, respuesta }) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const rotateAnim = useRef(new Animated.Value(0)).current;

  const flipCard = () => {
    Animated.timing(rotateAnim, {
      toValue: isFlipped ? 0 : 1,
      duration: 500,
      useNativeDriver: true,
    }).start(() => {
      setIsFlipped(!isFlipped);
    });
  };

  const frontInterpolate = rotateAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ["0deg", "180deg"],
  });

  const backInterpolate = rotateAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ["180deg", "360deg"],
  });

  // Colores para cada cara
  const frontColor = "#D4B2DA"; // Morado claro
  const backColor = "#543C3C"; // Café oscuro

  return (
    <TouchableOpacity onPress={flipCard} activeOpacity={0.8}>
      <View style={styles.cardContainer}>
        {/* Cara de la pregunta */}
        <Animated.View
          style={[
            styles.card,
            styles.cardFront,
            {
              transform: [{ rotateY: frontInterpolate }],
              backgroundColor: frontColor,
            },
          ]}
        >
          <Text style={styles.text}>{pregunta}</Text>
        </Animated.View>

        {/* Cara de la respuesta */}
        <Animated.View
          style={[
            styles.card,
            styles.cardBack,
            {
              transform: [{ rotateY: backInterpolate }],
              backgroundColor: backColor,
            },
          ]}
        >
          <Text style={styles.text}>{respuesta}</Text>
        </Animated.View>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  cardContainer: {
    width: 230,
    height: 340,
    alignItems: "center",
    justifyContent: "center",
  },
  card: {
    position: "absolute",
    width: 230,
    height: 340,
    backfaceVisibility: "hidden",
    borderRadius: 20,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  cardFront: {
    // backgroundColor: "#D4B2DA", // Morado claro (ahora se pasa dinámicamente)
  },
  cardBack: {
    // backgroundColor: "#543C3C", // Café oscuro (ahora se pasa dinámicamente)
    transform: [{ rotateY: "180deg" }],
  },
  text: {
    fontSize: 24,
    color: "white",
    textAlign: "center",
  },
});

export default Flashcard;