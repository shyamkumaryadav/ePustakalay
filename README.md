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

## Home Page Image  
![./docs/Image/LightDarkHome.png](./docs/Image/LightDarkHome.png)


### Django runserver
```bash  
cd ~/E_library
pipenv shell
pipenv install
# uncomment if you forget to do
# pipenv run make # for makemigrations
pipenv run migrate
# ./e_library/manage.py collectstatic
pipenv run start
# Starting development server at http://127.0.0.1:8000/

```