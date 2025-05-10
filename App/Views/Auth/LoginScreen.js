import React, { useState } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity } from 'react-native';
import LoginScreenViewModel from '../../viewmodels/LoginScreenViewModel';
import styles from '../../styles/LoginScreenStyles';

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const viewModel = new LoginScreenViewModel(navigation);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Iniciar Sesión</Text>
      <TextInput
        style={styles.input}
        placeholder="Nombre de usuario"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Contraseña"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Iniciar Sesión" onPress={() => viewModel.handleLogin(username, password)} color="#800080" />

      <Text style={styles.linkText}>
        ¿No tienes una cuenta?{' '}
        <TouchableOpacity onPress={() => viewModel.handleCreateAccount()}>
          <Text style={styles.link}>Crea una aquí</Text>
        </TouchableOpacity>
      </Text>
      <TouchableOpacity onPress={() => viewModel.handleForgotPassword()}>
        <Text style={styles.link}>¿Olvidaste tu contraseña?</Text>
      </TouchableOpacity>
    </View>
  );
};

export default LoginScreen;
