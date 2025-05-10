import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

const AuthToggle = ({ isLogin, onToggle }) => {
  return (
    <View style={styles.container}>
      <TouchableOpacity
        style={[styles.button, isLogin && styles.activeButton]}
        onPress={() => onToggle(true)}
      >
        <Text style={[styles.buttonText, isLogin && styles.activeButtonText]}>Login</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={[styles.button, !isLogin && styles.activeButton]}
        onPress={() => onToggle(false)}
      >
        <Text style={[styles.buttonText, !isLogin && styles.activeButtonText]}>Sign Up</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    marginBottom: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },
  button: {
    backgroundColor: 'transparent',
    borderWidth: 2,
    borderColor: '#800080',
    borderRadius: 20,
    marginHorizontal: 5,
    width: 110,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  activeButton: {
    backgroundColor: '#800080',
  },
  buttonText: {
    color: '#800080',
    textAlign: 'center',
    fontWeight: 'bold',
    paddingVertical: 10,
    fontSize: 16,
  },
  activeButtonText: {
    color: 'white',
  },
});

export default AuthToggle;