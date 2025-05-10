import React from 'react';
import { View, Image, StyleSheet } from 'react-native';

const RoundedImage = ({ source, style }) => {
  return (
    <View style={[styles.imageContainer, style]}>
      <Image source={source} style={styles.image} />
    </View>
  );
};

const styles = StyleSheet.create({
  imageContainer: {
    borderRadius: 20, // Ajusta el radio a tu gusto
    overflow: 'hidden', // Importante para que la imagen se ajuste al border radius
  },
  image: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover', // Ajusta la imagen al contenedor
  },
});

export default RoundedImage;