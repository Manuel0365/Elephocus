import { useEffect, useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as ImagePicker from 'expo-image-picker';
import { Alert } from 'react-native';

const useSettingsScreenViewModel = (navigation) => {
  const [profileImage, setProfileImage] = useState(null);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmNewPassword, setConfirmNewPassword] = useState('');
  const [currentUserId, setCurrentUserId] = useState(null);

  useEffect(() => {
    const loadCurrentUserId = async () => {
      const id = await AsyncStorage.getItem('currentUserId');
      setCurrentUserId(id);
    };
    loadCurrentUserId();
  }, []);

  useEffect(() => {
    if (currentUserId) {
      loadUserData(currentUserId);
    }
  }, [currentUserId]);

  const loadUserData = async (userId) => {
    try {
      const storedData = await AsyncStorage.getItem('users');
      const users = storedData ? JSON.parse(storedData) : [];
      const currentUser = users.find(u => u.id === userId);
      if (currentUser) {
        setUsername(currentUser.username);
        setEmail(currentUser.email);
        if (currentUser.profileImage) {
          setProfileImage(currentUser.profileImage);
        }
      }
    } catch (error) {
      console.error('Error al cargar datos:', error);
      Alert.alert('Error', 'Hubo un problema al cargar los datos del usuario.');
    }
  };

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!result.canceled) {
      setProfileImage(result.assets[0].uri);
    }
  };

  const handleUpdateProfile = async () => {
    try {
      const storedData = await AsyncStorage.getItem('users');
      const users = storedData ? JSON.parse(storedData) : [];
      const index = users.findIndex(u => u.id === currentUserId);

      if (index !== -1) {
        users[index].username = username;
        users[index].profileImage = profileImage;
        await AsyncStorage.setItem('users', JSON.stringify(users));
        Alert.alert('Éxito', 'Perfil actualizado correctamente.');
      }
    } catch (error) {
      console.error('Error al actualizar perfil:', error);
      Alert.alert('Error', 'Hubo un problema al actualizar el perfil.');
    }
  };

  const handleChangePassword = async () => {
    if (newPassword !== confirmNewPassword) {
      Alert.alert('Error', 'Las contraseñas no coinciden.');
      return;
    }

    try {
      const storedData = await AsyncStorage.getItem('users');
      const users = storedData ? JSON.parse(storedData) : [];
      const currentUser = users.find(u => u.id === currentUserId);

      if (currentUser && currentUser.password === currentPassword) {
        currentUser.password = newPassword;
        await AsyncStorage.setItem('users', JSON.stringify(users));
        Alert.alert('Éxito', 'Contraseña actualizada correctamente.');
        setCurrentPassword('');
        setNewPassword('');
        setConfirmNewPassword('');
      } else {
        Alert.alert('Error', 'La contraseña actual es incorrecta.');
      }
    } catch (error) {
      console.error('Error al cambiar contraseña:', error);
      Alert.alert('Error', 'Hubo un problema al cambiar la contraseña.');
    }
  };

  const handleLogout = async () => {
    try {
      await AsyncStorage.removeItem('currentUserId');
      navigation.reset({
        index: 0,
        routes: [{ name: 'Home' }],
      });
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
      Alert.alert('Error', 'Hubo un problema al cerrar sesión.');
    }
  };

  return {
    profileImage,
    username,
    email,
    currentPassword,
    newPassword,
    confirmNewPassword,
    pickImage,
    handleUsernameChange: setUsername,
    handleCurrentPasswordChange: setCurrentPassword,
    handleNewPasswordChange: setNewPassword,
    handleConfirmNewPasswordChange: setConfirmNewPassword,
    handleUpdateProfile,
    handleChangePassword,
    handleLogout
  };
};

export default useSettingsScreenViewModel;
