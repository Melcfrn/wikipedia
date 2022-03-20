# wikipedia
Projet Genie Logiciel Python

### Consignes
Afin de lancer correctement notre projet, il est conseillé de passer par un environnement virtuel et d'utiliser le fichier requirements.txt
```
conda create -n envname python=3.9
```
```
conda activate envname
```
```
pip install -r requirements.txt
```
```
python main/main.py
```

Pour réaliser les tests :
```
pytest -q test/TestExtractor.py
```
```
pytest -q test/TestConvertor.py
```
```
pytest -q test/TestSerializer.py
```
