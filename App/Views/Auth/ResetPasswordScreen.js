// ResetPasswordScreen.js (Vista)
import React, { useState } from 'react';
import { View, Text, TextInput, Button, Alert } from 'react-native';
import styles from '../../styles/ResetPasswordStyles';
import useResetPassword from '../../viewmodels/ResetPasswordViewModel';

const ResetPasswordScreen = ({ navigation }) => {
  const { email, setEmail, handleResetPassword } = useResetPassword(navigation);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Restablecer Contraseña</Text>
      <TextInput
        style={styles.input}
        placeholder="Correo electrónico"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
      />
      <Button title="Enviar" onPress={handleResetPassword} color="#800080" />
    </View>
  );
};

export default ResetPasswordScreen;
