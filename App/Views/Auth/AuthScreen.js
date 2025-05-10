import React from 'react';
import { View, Text, Image, TouchableOpacity, KeyboardAvoidingView, Platform, ScrollView, ImageBackground } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { observer } from 'mobx-react-lite';
import { useAuthViewModel } from '../../viewmodels/AuthViewModel';
import AuthToggle from '../../components/AuthToggle';
import LoginForm from '../../components/LoginForm';
import SignupForm from '../../components/SignupForm';
import styles from '../../styles/AuthScreenStyles.jsx';

const AuthScreen = observer(({ navigation }) => {
  const authViewModel = useAuthViewModel();

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === "ios" ? "padding" : "height"}
      style={styles.container}
    >
      <ImageBackground
        source={require('../../assets/background.jpeg')}
        style={styles.background}
      >
        <LinearGradient colors={['rgba(0,0,0,0.7)', 'transparent']} style={styles.gradientOverlay}>
          <ScrollView contentContainerStyle={styles.scrollViewContent} bounces={false}>
            <Image source={require('../../assets/logo.png')} style={styles.logo} />

            <View style={styles.formContainer}>
              <AuthToggle isLogin={authViewModel.isLogin} onToggle={authViewModel.setIsLogin} />
              <View style={styles.formCard}>
                {authViewModel.isLogin ? <LoginForm navigation={navigation}/> : <SignupForm />}
              </View>

              <TouchableOpacity style={styles.forgotPassword} onPress={() => navigation.navigate('ResetPassword')}>
                <Text style={styles.forgotPasswordText}>Forgot your password?</Text>
              </TouchableOpacity>
            </View>
          </ScrollView>
        </LinearGradient>
      </ImageBackground>
    </KeyboardAvoidingView>
  );
});

export default AuthScreen;