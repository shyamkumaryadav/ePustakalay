# E-library Managment System API

install [Git](https://git-scm.com/) or Download From Github  
Install [python 3](https://www.python.org/)  

### First Clone The Project  

```bash
$ pip install pipenv # to use script install or update pipenv with latest version
$ mkdir ~/E_library
$ cd ~/E_library
$ git clone git@github.com:shyamkumaryadav/e-library-management-system-api.git .
```  

## Home Page Image from <a href="//elibrarymanagementsystem.herokuapp.com/" title="go to Page"><img src="https://www3.assets.heroku.com/assets/logo-purple-08fb38cebb99e3aac5202df018eb337c5be74d5214768c90a8198c97420e4201.svg" width=70 style="background:pink;padding:2px;vertical-align:middle"></a>  
![./docs/Image/LightDarkHome.png](./docs/Image/LightDarkHome.png)


### Django runserver
```bash  
$ cd ~/E_library
$ pipenv shell
$ pipenv install
# uncomment if you forget to do
# $ pipenv run make # for makemigrations
$ pipenv run migrate
# $ pipenv run collect
$ pipenv run start
# Starting development server at http://0.0.0.0:8000/

```