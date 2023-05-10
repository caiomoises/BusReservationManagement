import streamlit as st
import os

# Obtém o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Concatena o diretório atual com o nome do arquivo
file_path = os.path.join(current_dir, 'tickets.txt')

def realizar_reserva(input_name, input_numBus, num_ticket):
    #Formatar a reserva como uma string separada por linhas
    reserva = f'Nome do passageiro: {input_name}\n' \
              f'Número do ônibus selecionado: {input_numBus}\n' \
              f'Número do ticket: {num_ticket}\n'

    #Ler as reservas existentes do arquivo
    reservas = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        reserva_atual = ''
        for line in file:
            line = line.strip()
            if line == '':
                reservas.append(reserva_atual)
                reserva_atual = ''
            else:
                reserva_atual += line + '\n'

    reservas.append(reserva) #Adicionar nova reserva à lista
    reservas.sort() #Ordenar a lista em ordem alfabética dos nomes

    with open(file_path, 'w') as file: #Escrever as reservas ordenadas de volta ao arquivo
        for reserva in reservas:
            file.write(reserva + '\n')
def excluir_reserva(nome):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        deleted = False
        for i in range(0, len(lines), 4):
            if lines[i].strip() == f'Nome do passageiro: {nome}':
                deleted = True
                continue
            file.write(lines[i])
            file.write(lines[i+1])
            file.write(lines[i+2])
            file.write(lines[i+3])

    if deleted:
        st.write(f"A reserva para {nome} foi excluída com sucesso.")
    else:
        st.write(f"Não foi encontrada uma reserva para {nome}.")
def listar_reservas():
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if len(lines) == 0:
        st.write("Não há reservas registradas.")
    else:
        for i in range(0, len(lines), 4):
            nome = lines[i].strip().split(': ')[1]
            num_bus = lines[i+1].strip().split(': ')[1]
            num_ticket = lines[i+2].strip().split(': ')[1]
            st.write(f"Nome do passageiro: {nome}")
            st.write(f"Número do ônibus selecionado: {num_bus}")
            st.write(f"Número do ticket: {num_ticket}")
            st.write('---')  
def buscar_reservas(nome):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    reservas_encontradas = []
    for i in range(0, len(lines), 4):
        nome_passageiro = lines[i].strip().split(': ')[1]
        if nome_passageiro.lower() == nome.lower():
            num_bus = lines[i+1].strip().split(': ')[1]
            num_ticket = lines[i+2].strip().split(': ')[1]
            reservas_encontradas.append((nome_passageiro, num_bus, num_ticket))

    if len(reservas_encontradas) == 0:
        st.write(f"Não foi encontrada nenhuma reserva para {nome}.")
    else:
        for reserva in reservas_encontradas:
            st.write('Reserva encontrada:')
            st.write(f"Nome do passageiro: {reserva[0]}")
            st.write(f"Número do ônibus selecionado: {reserva[1]}")
            st.write(f"Número do ticket: {reserva[2]}")
            st.write('---')
def editar_reserva(nome, new_bus,new_num_ticket):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        edited = False
        for i in range(0, len(lines), 4):
            if lines[i].strip() == f'Nome do passageiro: {nome}':

                # Escrever os novos dados da reserva no arquivo
                file.write(f'Nome do passageiro: {nome}\n')
                file.write(f'Número do ônibus selecionado: {new_bus}\n')
                file.write(f'Número do ticket: {new_num_ticket}\n')
                file.write(f'\n')

                edited = True
            else:
                file.write(lines[i])
                file.write(lines[i+1])
                file.write(lines[i+2])
                file.write(lines[i+3])

    if edited:
        st.write(f"A reserva para {nome} foi editada com sucesso.")
