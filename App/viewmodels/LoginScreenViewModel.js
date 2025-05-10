import AsyncStorage from '@react-native-async-storage/async-storage';
import { Alert } from 'react-native';

class LoginScreenViewModel {
  constructor(navigation) {
    this.navigation = navigation;
  }

  async handleLogin(username, password) {
    if (username === '' || password === '') {
      Alert.alert('Error', 'Por favor ingresa todos los campos.');
      return;
    }

    try {
      const userString = await AsyncStorage.getItem(username);
      if (userString === null) {
        Alert.alert('Error', 'Usuario no encontrado.');
        return;
      }

      const user = JSON.parse(userString);

      if (user.password === password) {
        Alert.alert('Éxito', `Bienvenido ${username}`);
        this.navigation.navigate('Main');
      } else {
        Alert.alert('Error', 'Contraseña incorrecta.');
      }

    } catch (error) {
      console.error(error);
      Alert.alert('Error', 'Hubo un problema al iniciar sesión.');
    }
  }

  handleCreateAccount() {
    this.navigation.navigate('Register');
  }

  handleForgotPassword() {
    Alert.alert('Redirigiendo a recuperación de contraseña...');
  }
}

export default LoginScreenViewModel;
