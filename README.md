# CS514L-CS22B046_CS22B059
## Assignment-3



### 🛠️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/Mokshith1708/AI-Assignment-3-Game-Playing
cd AI-Assignment-3-Game-Playing

```
#### 2. Install Dependencies
``` bash
pip install -r requirements.txt
```

#### 3. Setting up gym env
``` bash
git clone https://github.com/iamlucaswolf/gym-chess.git 
cd gym-chess
```
- In gym-chess folder open pyproject.toml file
- Go to the end of file and replace the below with the given
```bash
# before
[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

```bash
# After
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
```
- Now run this command 
```
python install -e.
```

#### 4. running the code
```bash
cd ..
python main.py
# choose the options displayed to run the code.
```
