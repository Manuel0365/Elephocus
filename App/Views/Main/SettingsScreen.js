import React from 'react';
import {
  View, Text, TextInput, TouchableOpacity, Image, ScrollView, SafeAreaView
} from 'react-native';
import useSettingsScreenViewModel from '../../viewmodels/SettingsScreenViewModel';
import styles from '../../styles/SettingsScreenStyles';
import BottomNavBar from '../../components/BottomNavBar';

const SettingsScreen = ({ navigation }) => {
  const {
    profileImage,
    username,
    email,
    currentPassword,
    newPassword,
    confirmNewPassword,
    pickImage,
    handleUsernameChange,
    handleCurrentPasswordChange,
    handleNewPasswordChange,
    handleConfirmNewPasswordChange,
    handleUpdateProfile,
    handleChangePassword,
    handleLogout
  } = useSettingsScreenViewModel(navigation);

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <TouchableOpacity onPress={pickImage} style={styles.imagePicker}>
          <Image
            source={profileImage ? { uri: profileImage } : require('../../assets/perfil-default.png')}
            style={styles.profileImage}
          />
          <Text style={styles.imagePickerText}>Cambiar foto de perfil</Text>
        </TouchableOpacity>

        <Text style={styles.label}>Nombre de Usuario:</Text>
        <TextInput
          style={styles.input}
          value={username}
          onChangeText={handleUsernameChange}
          placeholder="Nombre de Usuario"
        />

        <Text style={styles.label}>Correo Electrónico:</Text>
        <TextInput
          style={styles.input}
          value={email}
          editable={false}
          placeholder="Correo Electrónico"
        />

        <TouchableOpacity style={styles.updateButton} onPress={handleUpdateProfile}>
          <Text style={styles.updateButtonText}>Actualizar Perfil</Text>
        </TouchableOpacity>

        <Text style={styles.label}>Contraseña Actual:</Text>
        <TextInput
          style={styles.input}
          value={currentPassword}
          onChangeText={handleCurrentPasswordChange}
          placeholder="Contraseña Actual"
          secureTextEntry
        />

        <Text style={styles.label}>Nueva Contraseña:</Text>
        <TextInput
          style={styles.input}
          value={newPassword}
          onChangeText={handleNewPasswordChange}
          placeholder="Nueva Contraseña"
          secureTextEntry
        />

        <Text style={styles.label}>Confirmar Nueva Contraseña:</Text>
        <TextInput
          style={styles.input}
          value={confirmNewPassword}
          onChangeText={handleConfirmNewPasswordChange}
          placeholder="Confirmar Nueva Contraseña"
          secureTextEntry
        />

        <TouchableOpacity style={styles.updateButton} onPress={handleChangePassword}>
          <Text style={styles.updateButtonText}>Cambiar Contraseña</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.logoutButton} onPress={handleLogout}>
          <Text style={styles.logoutButtonText}>Cerrar Sesión</Text>
        </TouchableOpacity>
      </ScrollView>

      <View style={styles.bottomNavBar}>
        <BottomNavBar
          onHomePress={() => navigation.navigate('Main')}
          onBookPress={() => navigation.navigate('CatalogoFlashcards')}
          onAddPress={() => navigation.navigate('CrearFlashcard')}
          onListPress={() => navigation.navigate('CatalogoTemario')}
          onSettingsPress={() => navigation.navigate('Settings')}
          navigation={navigation}
        />
      </View>
    </SafeAreaView>
  );
};

export default SettingsScreen;
