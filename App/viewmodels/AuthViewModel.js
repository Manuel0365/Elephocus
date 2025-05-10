import { makeAutoObservable } from 'mobx';
import { useLocalObservable } from 'mobx-react-lite';

class AuthViewModel {
  isLogin = true;

  constructor() {
    makeAutoObservable(this);
  }

  setIsLogin = (value) => {
    this.isLogin = value;
  };
}

export const useAuthViewModel = () => useLocalObservable(() => new AuthViewModel());