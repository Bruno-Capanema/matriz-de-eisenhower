def coletar_atividades():
    """
    Coleta as atividades do usuário, pergunta sobre sua importância e urgência, 
    e as organiza em categorias da matriz de Eisenhower.
    """
    print("Bem-vindo ao programa de priorização baseado na Matriz de Eisenhower!")
    print("Você será perguntado sobre as atividades que deseja organizar e suas prioridades.")
    print("Para encerrar a coleta, digite 'acabou'.\n")
    
    # Dicionário para armazenar as categorias
    categorias = {
        "Alta prioridade (Muito importante e Urgente)": [],
        "Planejamento (Muito importante e Não urgente)": [],
        "Delegável (Menos importante e Urgente)": [],
        "Eliminável (Menos importante e Não urgente)": []
    }
    
    while True:
        # Coleta da atividade
        atividade = input("Digite a atividade (ou 'acabou' para finalizar): ").strip()
        if atividade.lower() == "acabou":
            break
        
        # Pergunta sobre a importância
        importancia = input("Essa atividade é muito importante? (sim/nao): ").strip().lower()
        while importancia not in ["sim", "nao"]:
            print("Por favor, responda com 'sim' ou 'nao'.")
            importancia = input("Essa atividade é muito importante? (sim/nao): ").strip().lower()
        
        # Pergunta sobre a urgência
        urgencia = input("Essa atividade é urgente? (sim/nao): ").strip().lower()
        while urgencia not in ["sim", "nao"]:
            print("Por favor, responda com 'sim' ou 'nao'.")
            urgencia = input("Essa atividade é urgente? (sim/nao): ").strip().lower()
        
        # Classificação da atividade
        if importancia == "sim" and urgencia == "sim":
            categorias["Alta prioridade (Muito importante e Urgente)"].append(atividade)
        elif importancia == "sim" and urgencia == "nao":
            categorias["Planejamento (Muito importante e Não urgente)"].append(atividade)
        elif importancia == "nao" and urgencia == "sim":
            categorias["Delegável (Menos importante e Urgente)"].append(atividade)
        else:
            categorias["Eliminável (Menos importante e Não urgente)"].append(atividade)
    
    return categorias


def exibir_resultados(categorias):
    """
    Exibe as atividades organizadas por prioridade.
    """
    print("\n===== RESULTADOS =====")
    for categoria, atividades in categorias.items():
        print(f"\n{categoria}:")
        if atividades:
            for atividade in atividades:
                print(f" - {atividade}")
        else:
            print(" (Nenhuma atividade cadastrada.)")


# Fluxo principal do programa
if __name__ == "__main__":
    # Coleta e organização das atividades
    categorias = coletar_atividades()
    # Exibição dos resultados
    exibir_resultados(categorias)
