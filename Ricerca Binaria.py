# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:32:33 2023

@author: Cristian
"""

def merge_sort(lista):
    if len(lista)>1:
        left_lista=lista[:len(lista)//2];  #1° lista parte da l'inizio al punto centro [Questa notazione speciale,serve che restituisce semplicemente la meta della lista]
        right_lista=lista[len(lista)//2:]; #2° va dal punto centrale alla fine della lista 
        
#Il termine "recursion=ricorsione" si riferisce a una funzione o a un processo che si auto-richiama
        
        merge_sort(left_lista);
        merge_sort(right_lista);
        
        # Merge
        i=0; #indice per left_lista
        j=0; #indice per right_lista
        
        traccia_i=0; # una terza variabile che tiene traccia dell'indice nell'array
        
        while i < len(left_lista) and j<len(right_lista):
            if left_lista[i]<right_lista[j]:
                lista[traccia_i]=left_lista[i];
                i+=1
#                traccia_i+=1;
            else:
                lista[traccia_i]=right_lista[j];
                j+=1;
            traccia_i+=1;
        
        while i<len(left_lista):
            lista[traccia_i]=left_lista[i];
            i+=1;
            traccia_i+=1;
        
        while j<len(right_lista):
            lista[traccia_i]= right_lista[j];
            j+=1;
            traccia_i +=1;

#Main
a = [2,3,5,8,9,23,45,0,7]
merge_sort(a);
print(a);

#%% si può divide la funzione?


def merge_sort(left_lista,right_lista,lista):
    i=0; #indice per left_lista
    j=0; #indice per right_lista
    traccia_i=0; # una terza variabile che tiene traccia dell'indice nell'array
    while i<len(left_lista) and j<len(right_lista):
        if left_lista[i]<right_lista[j]:
            lista[traccia_i]=left_lista[i];
            i+=1;
        else:
            lista[traccia_i]=right_lista[j];
            j+=1;
        traccia_i+=1;
        
    while i<len(left_lista):
        lista[traccia_i]=left_lista[i];
        i+=1;
        traccia_i+=1;
        
    while j<len(right_lista):
        lista[traccia_i]= right_lista[j];
        j+=1;
        traccia_i +=1;



def merge (lista,left_lista,right_lista):
    if len(lista)>1:
        
        
#Main
a = [2,3,5,8,9,23,45,0,7]
merge(a);
print(a);
#%%




def merge_sort(lista):
    if len(lista)>1:
        left_lista=lista[:len(lista)//2];  #1° lista parte da l'inizio al punto centro [Questa notazione speciale,serve che restituisce semplicemente la meta della lista]
        right_lista=lista[len(lista)//2:]; #2° va dal punto centrale alla fine della lista 
        
#Il termine "recursion=ricorsione" si riferisce a una funzione o a un processo che si auto-richiama
        
        merge_sort(left_lista);
        merge_sort(right_lista);
        
    # Merge
    i=0; #indice per left_lista
    j=0; #indice per right_lista
        
    traccia_i=0; # una terza variabile che tiene traccia dell'indice nell'array
        
    while i < len(left_lista) and j<len(right_lista):
        if left_lista[i]<right_lista[j]:
            lista[traccia_i]=left_lista[i];
            i+=1
#            traccia_i+=1;
        else:
            lista[traccia_i]=right_lista[j];
            j+=1;
        traccia_i+=1;
        
    while i<len(left_lista):
        lista[traccia_i]=left_lista[i];
        i+=1;
        traccia_i+=1;
        
    while j<len(right_lista):
        lista[traccia_i]= right_lista[j];
        j+=1;
        traccia_i +=1;

#Main
a = [2,3,5,8,9,23,45,0,7]
merge_sort(a);
print(a);










