import React from 'react';
import { View, Text, Image, ImageBackground, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import styles from '../../styles/HomeScreenStyles';

const HomeScreen = ({ navigation }) => { 
  const handleLogin = () => {
    navigation.navigate('Auth');
  };

  return (
    <ImageBackground
      source={require('../../assets/background.jpeg')}
      style={styles.background}
    >
      <LinearGradient
        colors={['rgba(0,0,0,0.7)', 'transparent']}
        style={styles.gradient}
      />

      <Image
        source={require('../../assets/logo.png')}
        style={styles.logo}
      />

      <Text style={styles.appName}>Elephocus</Text>

      <View style={styles.bottomContainer}>
        <TouchableOpacity style={styles.startButton} onPress={handleLogin}>
          <Text style={styles.startButtonText}>Iniciar</Text>
        </TouchableOpacity>

        <View style={styles.createAccountContainer}>
          <Text style={styles.noAccountText}>¿No tienes una cuenta? </Text>
          <TouchableOpacity onPress={handleLogin}>
            <Text style={styles.createAccountLink}>Crea una aquí</Text>
          </TouchableOpacity>
        </View>
      </View>
    </ImageBackground>
  );
};

export default HomeScreen;
