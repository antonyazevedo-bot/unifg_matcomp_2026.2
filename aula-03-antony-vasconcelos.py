# ==============================================================
# ATIVIDADE HAND-ON DE SALA — AULA 03
# Tema: Motor de Decisão Semafórica e Tabelas-Verdade (Squad SafeTraffic)
# Aluno: Antony Vasconcelos
# ==============================================================

def decidir_sinal_verde(ambulancia: bool, fluxo_alto: bool, 
                        pedestre: bool, cancela_trem: bool) -> bool:
    # Regra 1: Cancela férrea abaixada bloqueia qualquer avanço (Prioridade Máxima)
    if cancela_trem:
        return False
    
    # Regra 2: Ambulâncias têm prioridade absoluta no cruzamento
    if ambulancia:
        return True
    
    # Regra 3: Fluxo alto com preferência para pedestres (só abre se não houver pedestre)
    return fluxo_alto and not pedestre


# Bateria de Asserções (Testes automatizados exigidos pelo professor)
assert decidir_sinal_verde(True, False, True, False) == True, "Erro no teste 1"
assert decidir_sinal_verde(False, True, False, False) == True, "Erro no teste 2"
assert decidir_sinal_verde(False, True, True, False) == False, "Erro no teste 3"
assert decidir_sinal_verde(True, True, True, True) == False, "Erro no teste 4"
assert decidir_sinal_verde(False, False, False, False) == False, "Erro no teste 5"

print("SUCESSO: TODAS AS REGRAS LÓGICAS HOMOLOGADAS!")
