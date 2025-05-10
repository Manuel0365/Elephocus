// viewmodels/HomeScreenViewModel.js

import { useState } from 'react';

const useHomeScreenViewModel = (navigation) => {
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = () => {
    setIsLoading(true);
    navigation.navigate('Auth');
    setIsLoading(false);
  };

  return {
    isLoading,
    handleLogin,
  };
};

export default useHomeScreenViewModel;
