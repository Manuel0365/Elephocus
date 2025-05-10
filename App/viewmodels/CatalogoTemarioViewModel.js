import { makeAutoObservable } from "mobx";

class CatalogoTemarioViewModel {
  temas = ["Matemáticas", "Historia", "Ciencias", "Inglés"];

  constructor() {
    makeAutoObservable(this);
  }

  cargarTemas() {
    // No es necesario cargar desde AsyncStorage en este caso,
    // pero podrías hacerlo si quieres persistir los temas.
  }

  agregarTema(tema) {
    this.temas.push(tema);
  }

  eliminarTema(tema) {
    this.temas = this.temas.filter((t) => t !== tema);
  }
}

export const useCatalogoTemarioViewModel = () => new CatalogoTemarioViewModel();