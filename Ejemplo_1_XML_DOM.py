#!/usr/bin/env python
# coding: utf-8

# In[5]:


from xml.dom.minidom  import parse
import xml.dom.minidom 

ArbolDom = xml.dom.minidom.parse("datos.xml")
libros = ArbolDom.getElementsByTagName("Libro")

for libro in libros:
    isbn = libro.getAttribute("isbn")
    print("isbn:", isbn)
    
    titulo = libro.getElementsByTagName("titulo")[0]
    print("titulo:", titulo.firstChild.data)
    
    fecha = libro.getElementsByTagName("fecha")[0]
    print("fecha:", fecha.firstChild.data)
    
    autores = libro.getElementsByTagName("autor")
    for autor in autores:
        print("autor:", autor.firstChild.data)
    
    print("-----")
            
    


# In[ ]:




