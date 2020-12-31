def notas(*n, sit=False):
    '''
    -> Analisa
    :param n: Notas a serem recebidas para analise de um aluno ou turma
    :param sit: Valor opcional, indicando se deve ou não mostrar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    '''

    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n) / len(n)
    if sit:
        if turma['media'] > 8:
            turma['situação'] = 'Boa'
        elif turma['media'] < 8:
            turma['situação'] = 'Razoavél'
        else:
            turma['situação'] = 'Péssima'
    print(turma)


notas(2, 8, 9,sit=True)