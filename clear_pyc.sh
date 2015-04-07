#!/bin/bash
# borrar los ficheros compilados de Python
find . -name *.pyc -type f -print0 | xargs -0 /bin/rm -f -r
# borrar un fichero oculto
find . -name .fuse_ -type f -print0 | xargs -0 /bin/rm -f -r
