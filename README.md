# DPKG CKAN

## Utilização

- Terminal

```
$ pip install dpkgckan
```

- Arquivo Python
```
# Publicar
from dpkgckanmg.functions import publish
publish(path/dir/datapackage, ckan_key)

# Criar Recurso
from dpkgckanmg.functions import criarArquivo2
criarArquivo2(1, 2, 3)

# Atualizar Data Set
from dpkgckanmg.functions import dataSet
dataSet(1, 2, 3)

# Atualizar Recurso
from dpkgckanmg.functions import resource
resource(1, 2, 3)


### 1,2 3 deveráo ser retirados do arquivo .doc (gabriel atualizará)
```
