# -*- coding: utf-8 -*-
"""AnáliseCFD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kTUNYHgjH7UntvXlofrXh28P4QfWYITU
"""

## UNIVERSIDADE FEDERAL DO RIO DE JANEIRO - CAMPUS MACAÉ
## ACADÊMICO: ENTHONY CARMO COSTA          DRE:119055306

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def P1(num):
  t=[]
  for i in range(0,num-1):
      t.append(i)

      nome=('extract.'+str(i)+'.csv')
      arquivo = open(nome,'r+')
      arquivo_csv = csv.reader(arquivo,delimiter=",")

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      for i,linha in enumerate(arquivo_csv):
        if i ==0:
          continue
        else:
          for linhascolunas in arquivo_csv:
            if linhascolunas[0]=='1.#QNANe+0000' or linhascolunas[0]=='1.#QNANe+000':
              linhascolunas[0]="0"
              p.append(float(linhascolunas[0]))
            else:
              p.append(float(linhascolunas[0]))
            if linhascolunas[1]=='1.#QNANe+0000' or linhascolunas[1]=='1.#QNANe+000':
              linhascolunas[1]="0"
              u.append(float(linhascolunas[1]))
            else:
              u.append(float(linhascolunas[1]))
            if linhascolunas[2]=='1.#QNANe+0000' or linhascolunas[2]=='1.#QNANe+000':
              linhascolunas[2]="0"
              v.append(float(linhascolunas[2]))
            else:
              v.append(float(linhascolunas[2]))
            if linhascolunas[3]=='1.#QNANe+0000' or linhascolunas[3]=='1.#QNANe+000':
              linhascolunas[3]="0"
              w.append(float(linhascolunas[3]))
            else:
              w.append(float(linhascolunas[3]))
            if linhascolunas[9]=='1.#QNANe+0000' or linhascolunas[9]=='1.#QNANe+000':
              linhascolunas[9]="0"
              x1.append(float(linhascolunas[9]))
            else:
              x1.append(float(linhascolunas[9]))
            if linhascolunas[10]=='1.#QNANe+0000' or linhascolunas[10]=='1.#QNANe+000':
              linhascolunas[10]="0"
              x2.append(float(linhascolunas[10]))
            else:
              x2.append(float(linhascolunas[10]))
            if linhascolunas[11]=='1.#QNANe+0000' or linhascolunas[11]=='1.#QNANe+000':
              linhascolunas[11]="0"
              x3.append(float(linhascolunas[11]))
            else:
              x3.append(float(linhascolunas[11]))
            
      ## ADICIONAR LEITOR
      
      plt.plot(x1,p)
      plt.title('Perfil da pressão em x')
      plt.xlabel('x')
      plt.ylabel('p')

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]
      
      arquivo.close()

def P2(num):
  t=[]
  for i in range(0,num-1):
      t.append(i)

      nome=('extract.'+str(i)+'.csv')
      arquivo = open(nome,'r')
      arquivo_csv = csv.reader(arquivo,delimiter=",")

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      for i,linha in enumerate(arquivo_csv):
        if i ==0:
          continue
        else:
          for linhascolunas in arquivo_csv:
            if linhascolunas[0]=='1.#QNANe+0000' or linhascolunas[0]=='1.#QNANe+000':
              linhascolunas[0]="0"
              p.append(float(linhascolunas[0]))
            else:
              p.append(float(linhascolunas[0]))
            if linhascolunas[1]=='1.#QNANe+0000' or linhascolunas[1]=='1.#QNANe+000':
              linhascolunas[1]="0"
              u.append(float(linhascolunas[1]))
            else:
              u.append(float(linhascolunas[1]))
            if linhascolunas[2]=='1.#QNANe+0000' or linhascolunas[2]=='1.#QNANe+000':
              linhascolunas[2]="0"
              v.append(float(linhascolunas[2]))
            else:
              v.append(float(linhascolunas[2]))
            if linhascolunas[3]=='1.#QNANe+0000' or linhascolunas[3]=='1.#QNANe+000':
              linhascolunas[3]="0"
              w.append(float(linhascolunas[3]))
            else:
              w.append(float(linhascolunas[3]))
            if linhascolunas[9]=='1.#QNANe+0000' or linhascolunas[9]=='1.#QNANe+000':
              linhascolunas[9]="0"
              x1.append(float(linhascolunas[9]))
            else:
              x1.append(float(linhascolunas[9]))
            if linhascolunas[10]=='1.#QNANe+0000' or linhascolunas[10]=='1.#QNANe+000':
              linhascolunas[10]="0"
              x2.append(float(linhascolunas[10]))
            else:
              x2.append(float(linhascolunas[10]))
            if linhascolunas[11]=='1.#QNANe+0000' or linhascolunas[11]=='1.#QNANe+000':
              linhascolunas[11]="0"
              x3.append(float(linhascolunas[11]))
            else:
              x3.append(float(linhascolunas[11]))
          
      
    

      ## ADICIONAR LEITOR
      
      plt.plot(x2,p)
      plt.title('Perfil da pressão em y')
      plt.xlabel('y')
      plt.ylabel('p')

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      arquivo.close()
def P3(num):
  t=[]
  for i in range(0,num-1):
      t.append(i)

      nome=('extract.'+str(i)+'.csv')
      arquivo = open(nome,'r')
      arquivo_csv = csv.reader(arquivo,delimiter=",")

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      for i,linha in enumerate(arquivo_csv):
        if i ==0:
          continue
        else:
          for linhascolunas in arquivo_csv:
            if linhascolunas[0]=='1.#QNANe+0000' or linhascolunas[0]=='1.#QNANe+000':
              linhascolunas[0]="0"
              p.append(float(linhascolunas[0]))
            else:
              p.append(float(linhascolunas[0]))
            if linhascolunas[1]=='1.#QNANe+0000' or linhascolunas[1]=='1.#QNANe+000':
              linhascolunas[1]="0"
              u.append(float(linhascolunas[1]))
            else:
              u.append(float(linhascolunas[1]))
            if linhascolunas[2]=='1.#QNANe+0000' or linhascolunas[2]=='1.#QNANe+000':
              linhascolunas[2]="0"
              v.append(float(linhascolunas[2]))
            else:
              v.append(float(linhascolunas[2]))
            if linhascolunas[3]=='1.#QNANe+0000' or linhascolunas[3]=='1.#QNANe+000':
              linhascolunas[3]="0"
              w.append(float(linhascolunas[3]))
            else:
              w.append(float(linhascolunas[3]))
            if linhascolunas[9]=='1.#QNANe+0000' or linhascolunas[9]=='1.#QNANe+000':
              linhascolunas[9]="0"
              x1.append(float(linhascolunas[9]))
            else:
              x1.append(float(linhascolunas[9]))
            if linhascolunas[10]=='1.#QNANe+0000' or linhascolunas[10]=='1.#QNANe+000':
              linhascolunas[10]="0"
              x2.append(float(linhascolunas[10]))
            else:
              x2.append(float(linhascolunas[10]))
            if linhascolunas[11]=='1.#QNANe+0000' or linhascolunas[11]=='1.#QNANe+000':
              linhascolunas[11]="0"
              x3.append(float(linhascolunas[11]))
            else:
              x3.append(float(linhascolunas[11]))
    

      ## ADICIONAR LEITOR
      
      plt.plot(x3,p)
      plt.title('Perfil da pressão em z')
      plt.xlabel('z')
      plt.ylabel('p')

      


      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      arquivo.close()

def V1(num):
  t=[]
  for i in range(0,num-1):
      t.append(i)

      nome=('extract.'+str(i)+'.csv')
      arquivo = open(nome,'r')
      arquivo_csv = csv.reader(arquivo,delimiter=",")

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      for i,linhascolunas in enumerate(arquivo_csv):
        if i ==0:
          continue
        else:
          for linhascolunas in arquivo_csv:
            if linhascolunas[0]=='1.#QNANe+0000' or linhascolunas[0]=='1.#QNANe+000':
              linhascolunas[0]="0"
              p.append(float(linhascolunas[0]))
            else:
              p.append(float(linhascolunas[0]))
            if linhascolunas[1]=='1.#QNANe+0000' or linhascolunas[1]=='1.#QNANe+000':
              linhascolunas[1]="0"
              u.append(float(linhascolunas[1]))
            else:
              u.append(float(linhascolunas[1]))
            if linhascolunas[2]=='1.#QNANe+0000' or linhascolunas[2]=='1.#QNANe+000':
              linhascolunas[2]="0"
              v.append(float(linhascolunas[2]))
            else:
              v.append(float(linhascolunas[2]))
            if linhascolunas[3]=='1.#QNANe+0000' or linhascolunas[3]=='1.#QNANe+000':
              linhascolunas[3]="0"
              w.append(float(linhascolunas[3]))
            else:
              w.append(float(linhascolunas[3]))
            if linhascolunas[9]=='1.#QNANe+0000' or linhascolunas[9]=='1.#QNANe+000':
              linhascolunas[9]="0"
              x1.append(float(linhascolunas[9]))
            else:
              x1.append(float(linhascolunas[9]))
            if linhascolunas[10]=='1.#QNANe+0000' or linhascolunas[10]=='1.#QNANe+000':
              linhascolunas[10]="0"
              x2.append(float(linhascolunas[10]))
            else:
              x2.append(float(linhascolunas[10]))
            if linhascolunas[11]=='1.#QNANe+0000' or linhascolunas[11]=='1.#QNANe+000':
              linhascolunas[11]="0"
              x3.append(float(linhascolunas[11]))
            else:
              x3.append(float(linhascolunas[11]))
      
    

      ## ADICIONAR LEITOR
      
      plt.title('Velocidade u em x:')
      plt.xlabel('x')
      plt.ylabel('v')
      plt.plot(x1,u)
      


      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      arquivo.close()
      
def V2(num):
  t=[]
  for i in range(0,num-1):
      t.append(i)

      nome=('extract.'+str(i)+'.csv')
      arquivo = open(nome,'r')
      arquivo_csv = csv.reader(arquivo,delimiter=",")

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      for i,linhascolunas in enumerate(arquivo_csv):
        if i ==0:
          continue
        else:
          for linhascolunas in arquivo_csv:
            if linhascolunas[0]=='1.#QNANe+0000' or linhascolunas[0]=='1.#QNANe+000':
              linhascolunas[0]="0"
              p.append(float(linhascolunas[0]))
            else:
              p.append(float(linhascolunas[0]))
            if linhascolunas[1]=='1.#QNANe+0000' or linhascolunas[1]=='1.#QNANe+000':
              linhascolunas[1]="0"
              u.append(float(linhascolunas[1]))
            else:
              u.append(float(linhascolunas[1]))
            if linhascolunas[2]=='1.#QNANe+0000' or linhascolunas[2]=='1.#QNANe+000':
              linhascolunas[2]="0"
              v.append(float(linhascolunas[2]))
            else:
              v.append(float(linhascolunas[2]))
            if linhascolunas[3]=='1.#QNANe+0000' or linhascolunas[3]=='1.#QNANe+000':
              linhascolunas[3]="0"
              w.append(float(linhascolunas[3]))
            else:
              w.append(float(linhascolunas[3]))
            if linhascolunas[9]=='1.#QNANe+0000' or linhascolunas[9]=='1.#QNANe+000':
              linhascolunas[9]="0"
              x1.append(float(linhascolunas[9]))
            else:
              x1.append(float(linhascolunas[9]))
            if linhascolunas[10]=='1.#QNANe+0000' or linhascolunas[10]=='1.#QNANe+000':
              linhascolunas[10]="0"
              x2.append(float(linhascolunas[10]))
            else:
              x2.append(float(linhascolunas[10]))
            if linhascolunas[11]=='1.#QNANe+0000' or linhascolunas[11]=='1.#QNANe+000':
              linhascolunas[11]="0"
              x3.append(float(linhascolunas[11]))
            else:
              x3.append(float(linhascolunas[11]))
      
    

      ## ADICIONAR LEITOR
      
      plt.title('Velocidade v em x:')
      plt.xlabel('y')
      plt.ylabel('v')
      plt.plot(x1,v)

      


      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      arquivo.close()
def V3(num):
  t=[]
  
  for i in range(0,num-1):
      t.append(i)

      nome=('extract.'+str(i)+'.csv')
      arquivo = open(nome,'r')
      arquivo_csv = csv.reader(arquivo,delimiter=",")

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      for i,linha in enumerate(arquivo_csv):
        if i ==0:
          continue
        else:
          for linhascolunas in arquivo_csv:
            if linhascolunas[0]=='1.#QNANe+0000' or linhascolunas[0]=='1.#QNANe+000':
              linhascolunas[0]="0"
              p.append(float(linhascolunas[0]))
            else:
              p.append(float(linhascolunas[0]))
            if linhascolunas[1]=='1.#QNANe+0000' or linhascolunas[1]=='1.#QNANe+000':
              linhascolunas[1]="0"
              u.append(float(linhascolunas[1]))
            else:
              u.append(float(linhascolunas[1]))
            if linhascolunas[2]=='1.#QNANe+0000' or linhascolunas[2]=='1.#QNANe+000':
              linhascolunas[2]="0"
              v.append(float(linhascolunas[2]))
            else:
              v.append(float(linhascolunas[2]))
            if linhascolunas[3]=='1.#QNANe+0000' or linhascolunas[3]=='1.#QNANe+000':
              linhascolunas[3]="0"
              w.append(float(linhascolunas[3]))
            else:
              w.append(float(linhascolunas[3]))
            if linhascolunas[9]=='1.#QNANe+0000' or linhascolunas[9]=='1.#QNANe+000':
              linhascolunas[9]="0"
              x1.append(float(linhascolunas[9]))
            else:
              x1.append(float(linhascolunas[9]))
            if linhascolunas[10]=='1.#QNANe+0000' or linhascolunas[10]=='1.#QNANe+000':
              linhascolunas[10]="0"
              x2.append(float(linhascolunas[10]))
            else:
              x2.append(float(linhascolunas[10]))
            if linhascolunas[11]=='1.#QNANe+0000' or linhascolunas[11]=='1.#QNANe+000':
              linhascolunas[11]="0"
              x3.append(float(linhascolunas[11]))
            else:
              x3.append(float(linhascolunas[11]))
      
    

      ## ADICIONAR LEITOR
      
      plt.title('Velocidade w em x:')
      plt.xlabel('x')
      plt.ylabel('w')
      plt.plot(x1,w)

      u=[]
      v=[]
      w=[]

      x1=[]
      x2=[]
      x3=[]

      p =[]

      arquivo.close()

N=10

P1(N)

P2(N)

P3(N)

V1(N)

V2(N)

V3(N)