// ResetPasswordViewModel.js
import { useState } from 'react';
import { Alert } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const useResetPassword = (navigation) => {
  const [email, setEmail] = useState('');

  const handleResetPassword = async () => {
    if (!email) {
      Alert.alert('Error', 'Por favor ingresa tu correo electrónico.');
      return;
    }

    try {
      const userString = await AsyncStorage.getItem(email);
      if (!userString) {
        Alert.alert('Error', 'Correo no registrado.');
        return;
      }

      Alert.alert('Éxito', 'Se ha enviado un enlace de recuperación.');
      navigation.navigate('Login');
    } catch (error) {
      console.error('Error al restablecer contraseña:', error);
      Alert.alert('Error', 'Ocurrió un problema. Inténtalo de nuevo.');
    }
  };

  return { email, setEmail, handleResetPassword };
};

export default useResetPassword;
