
# coding: utf-8

# In[1]:


import os


# In[7]:


base_dir = str(input('Ingrese la ruta para cambiar nombre a archivos:'))
fix_dir = base_dir.replace("\\", "/")

name = str(input('Ingrese el nombre base para los nuevos archivos:'))
extension = str(input('Ingrese la extensión de sus archivos -.jpg; .png; etc... - : '))


contador = 0
files_max = len(os.listdir(fix_dir)) - 1
files = os.listdir(fix_dir)
old_name = ''
new_name = ''

#file_max es -1 por el archivo oculto thumb.db.
#En ocasiones, thumb.db igual cambia de nombre. Hay que controlar esto de forma más efectiva.

while contador <= files_max:
    #Obtener nombre archivo uno por uno.
    old_name = files[contador]
    
    #Crear el nuevo nombre.
    new_name = name + '_' + str(contador) + extension
    
    #Renombrar el archivo antiguo.
    os.rename(os.path.join(fix_dir, old_name), os.path.join(fix_dir, new_name))
    
    print('Nombre antiguo:', old_name ,' ', 'Nombre nuevo:', new_name)
    contador += 1

