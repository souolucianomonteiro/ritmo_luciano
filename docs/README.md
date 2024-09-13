# Django template for a new django CMS 4 project

A Django template for a typical django CMS installation with no 
special bells or whistles. It is supposed as a starting point 
for new projects.

If you prefer a different set of template settings, feel free to 
create your own templates by cloning this repo.

To install django CMS 4 by hand type the following commands:

1. Create virtual environment and activate it
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install Django, django CMS and other required packages
   ```
   pip install django-cms
   ```
3. Create project `<<project_name>>` using this template
   ```
   djangocms <<project_name>>
   cd <<project_name>>
   ```
4. Run testserver
   ```
   ./manage.py runserver
   ```

Note: If you run into a problem of missing dependencies, please
update `pip` using `pip install -U pip` before running the 
`djangocms` command.

# atualiza as dependências 
pip-compile requirements.in
# instala as dependências 
pip install -r requirements.txt
# sincroniza os ambientes
pip-sync
# prepara os arquivos para persistência
python manage.py makemigrations
# migrate banco bd postgres
python manage.py migrate --database=default
# executa o servidor djanfo
python manage.py runserver

# as importações de material desing deve ser: 
from viewflow.material import SomeClass


# iniciar repositório local 
git init

# listar todos os arquivos, incluindo arquivos ocultos, 
Get-ChildItem -Force

# consultar em qual branch está:
git branch

# criar uma nova branch 
git checkout -b feature/models

# ir para uma branch criada ou mudar de branch
git checkout nome-da-branch

# listar as branches locais e remotas
git branch -a

# desenvolver e adicionar arquivos ao índice
git add .

# fazer um commit 
git commit -m "Descrição do que foi feito"

# verificar o histórico do commits
git log

# enviar a branch para o repositório remoto
git push origin nome-da-branch

# fazer o merge da branch secundária na principal
# o merge deve ser feiro da branch que vai ser atualizada.
# a branch a ser informada é da qual as informações serão importadas.  
git merge nome-da-branch 

# commit de resolução de conflitos do merge
git add .
git commit -m "Resolve conflitos de merge"

# puxa as alterações da branch main no repositório remoto origin para o local.
git pull origin main

# "envia minhas alterações do local para a branch main no repositório remoto origin".
git push origin main

#  verificar se "origin" é o nome do repositório remoto padrão e quais repositórios remotos estão configurados, use:
git remote -v

# para atualizar a branch remota com as mudanças feitas localmente na branch
# quando local e remoto estão sincronizados. 
git push origin feature/models

# verificar se há alguma diferença entre a branch local e a remota usando:
git fetch origin
git status

# para comparar os commits entre a branch local e a remota:
git log origin/feature/models..feature/models

# confirmar que a branch local está rastreando a branch remota:
git branch -vv
