
# Curso de LangChain para Principiantes
<!-- Si estás acá, lo más probable es que me sigas en Youtube. -->

### ¿Cómo iniciar?
1. Crea un nuevo entorno virtual
```python 
py -m venv venv
```

2. Entra en el entorno virtual
```python 
source venv/Scripts/activate
```

3. Instala las dependencias
```python 
pip install -r requirements.txt
```

4. Copia el archivo .env.example a uno .env
```bash
cp .env.example .env
```

5. Agrega la llave OPENAI_API_KEY en el archivo .env
```env
OPENAI_API_KEY=tu_llave_aqui
```

### Contribuir
Si deseas contribuir a este proyecto, por favor sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

### Recursos Adicionales
- [Documentación de LangChain](https://python.langchain.com/v0.2/docs/introduction/)
- [API de OpenAI](https://platform.openai.com/docs/overview)