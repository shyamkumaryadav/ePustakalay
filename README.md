# E-library Managment System API

install [Git](https://git-scm.com/) or Download From Github  
Install [python 3](https://www.python.org/)  

### First Clone The Project  

```bash
pip install pipenv # use what you have
mkdir ~/E_library
cd ~/E_library
git clone git@github.com:shyamkumaryadav/e-library-management-system-api.git .
```  


### Django runserver
```bash  
cd ~/E_library
pipenv shell
pipenv install
# uncomment if you forget to do
# ./e_library/manage.py makemigrations
python e_library/manage.py migrate
# ./e_library/manage.py collectstatic
python e_library/manage.py runserver
# Starting development server at http://127.0.0.1:8000/

```