# E-library Managment System

Install Node
Install python 3

### First Clone The Project  

```bash
pip install pipenv
mkdir ~/E_library
cd ~/E_library
git clone git@github.com:shyamkumaryadav/e-library-management-system.git .
```

### npm build
```bash  
cd ~/E_library/e_library
# Note: first check package.json file present at this location if yes follow this step
npm install # or use npm i 
npm run build
```

### Django runserver
```bash  
cd ~/E_library
pipenv shell
# uncomment if you forget to do
# ./e_library/manage.py makemigrations
# ./e_library/manage.py migrate
# ./e_library/manage.py collectstatic
./e_library/manage.py runserver
# Starting development server at http://127.0.0.1:8000/

```