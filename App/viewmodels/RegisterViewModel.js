import AsyncStorage from '@react-native-async-storage/async-storage';

class RegisterViewModel {
  async handleRegister(email, username, password, confirmPassword, onSuccess, onError) {
    if (!email || !username || !password || !confirmPassword) {
      onError('Por favor completa todos los campos.');
      return;
    }

    if (password !== confirmPassword) {
      onError('Las contraseñas no coinciden.');
      return;
    }

    try {
      const storedUsers = await AsyncStorage.getItem('users');
      const users = storedUsers ? JSON.parse(storedUsers) : [];

      if (users.some(user => user.email === email || user.username === username)) {
        onError('Este correo o nombre de usuario ya está registrado.');
        return;
      }

      const newUser = { id: Date.now().toString(), email, username, password };
      users.push(newUser);
      await AsyncStorage.setItem('users', JSON.stringify(users));

      onSuccess('Usuario registrado correctamente.');
    } catch (error) {
      console.error('Error al registrar usuario:', error);
      onError('Hubo un problema al registrar el usuario.');
    }
  }
}

export default new RegisterViewModel();
