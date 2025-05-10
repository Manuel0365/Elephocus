import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 16,
    backgroundColor: '#FFFFFF',
  },
  title: {
    fontSize: 24,
    marginBottom: 24,
    textAlign: 'center',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 12,
    paddingLeft: 8,
  },
  linkText: {
    textAlign: 'center',
    marginTop: 10,
  },
  link: {
    color: '#800080',
    textDecorationLine: 'underline',
    textAlign: 'center'
  },
});

export default styles;
