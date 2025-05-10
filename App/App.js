import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './Views/Main/HomeScreen';
import MainScreen from './Views/Main/MainScreen';
import CrearFlashcardScreen from './Views/Flashcards/CreateFlashcard';
import CatalogoFlashcardsScreen from './Views/Flashcards/CatalogueFlashcards';
import RegisterScreen from './Views/Auth/RegisterScreen';
import AuthScreen from './Views/Auth/AuthScreen';
import SettingsScreen from './Views/Main/SettingsScreen';
import CatalogoTemario from './Views/Flashcards/CatalogoTemario';
import ResetPasswordScreen from './Views/Auth/ResetPasswordScreen';
import { useFonts } from 'expo-font';

const Stack = createStackNavigator();

const App = () => {
  const [fontsLoaded] = useFonts({
    'Oleo Script': require('./assets/fonts/OleoScript-Regular.ttf'),
    'Oleo Script Bold': require('./assets/fonts/OleoScript-Bold.ttf')
  });

  if (!fontsLoaded) {
    return null;
  }

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} options={{ headerShown: false }} />
        <Stack.Screen name="Auth" component={AuthScreen} options={{ headerShown: false }} />
        <Stack.Screen name="Main" component={MainScreen} options={{ headerShown: false }} />
        <Stack.Screen name="ResetPassword" component={ResetPasswordScreen} options={{ headerShown: false }} />
        <Stack.Screen name="CrearFlashcard" component={CrearFlashcardScreen} options={{ headerShown: false }} />
        <Stack.Screen name="CatalogoFlashcards" component={CatalogoFlashcardsScreen} options={{ headerShown: false }} />
        <Stack.Screen name="Register" component={RegisterScreen} options={{ headerShown: false }} />
        <Stack.Screen name="Settings" component={SettingsScreen} options={{ headerShown: false }} />
        <Stack.Screen name="CatalogoTemario" component={CatalogoTemario} options={{ headerShown: false }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;