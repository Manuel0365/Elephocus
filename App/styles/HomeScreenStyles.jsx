import { StyleSheet } from 'react-native';

const HomeScreenStyles = StyleSheet.create({
  background: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  gradient: {
    position: 'absolute',
    left: 0,
    right: 0,
    bottom: 0,
    height: '100%', 
  },
  logo: {
    width: 170,
    height: 220,
    resizeMode: 'contain',
    marginBottom: 20,
    position: 'absolute',
    top: 50,
  },
  appName: {
    fontSize: 40,
    fontWeight: 'bold',
    color: '#A5A5A5',
    marginBottom: 50,
    position: 'absolute',
    top: 260, 
    textAlign: 'center',
  },
  bottomContainer: {
    position: 'absolute',
    bottom: 50,
    width: '80%',
    alignItems: 'center',
    top: 650, 
  },
  startButton: {
    backgroundColor: '#800080', 
    paddingVertical: 15, 
    paddingHorizontal: 40,
    borderRadius: 30, 
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 20, 
    width: '100%',
  },
  startButtonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
  createAccountContainer: {
    flexDirection: 'row', 
    alignItems: 'center',
    justifyContent: 'center',
  },
  noAccountText: {
    color: '#D5D5D5',
    fontSize: 16,
    fontWeight: 'bold',
  },
  createAccountLink: {
    color: '#800080', 
    fontSize: 16,
    textDecorationLine: 'underline', 
  },
});

export default HomeScreenStyles;
