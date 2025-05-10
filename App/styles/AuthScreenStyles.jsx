import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: { flex: 1 },
  background: { flex: 1, width: '100%', height: '100%' },
  gradientOverlay: { 
    position: 'absolute', 
    left: 0, 
    right: 0, 
    top: 0, 
    bottom: 0, 
    alignItems: 'center', 
    justifyContent: 'center' 
  },
  scrollViewContent: { 
    flexGrow: 1, 
    alignItems: 'center', 
    justifyContent: 'center', 
    paddingVertical: 20 
  },
  logo: { 
    width: 150, 
    height: 200, 
    resizeMode: 'contain', 
    marginBottom: 20, 
    marginTop: 50 
  },
  formContainer: { 
    width: '80%', 
    alignItems: 'center', 
    marginBottom: 5 
  },
  formCard: { 
    width: '100%', 
    backgroundColor: 'rgba(255, 255, 255, 0.8)', 
    borderRadius: 10, 
    padding: 15 
  },
  forgotPassword: { 
    marginTop: 15 
  },
  forgotPasswordText: { 
    color: '#000000', 
    fontSize: 16 
  },
});

export default styles;