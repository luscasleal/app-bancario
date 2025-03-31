from models import Conta, engine, Bancos, Status, Historico, Tipos
from sqlmodel import Session, select
from datetime import date, timedelta

def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco==conta.banco)
        results = session.exec(statement).all()
        
        if results:
            print('Já existe conta neste banco"')
            return
        
        session.add(conta)
        session.commit()
        return conta

def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        results = session.exec(statement).all()
    return results

def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id)
        conta = session.exec(statement).first()
        if conta.valor > 0:
             raise ValueError('Essa conta aidna possui saldo')
        conta.status = Status.INVATIVO
        session.commit()

def transferir_saldo(id_saida, id_destino, transfered_ammount):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id_saida)
        conta_saida = session.exec(statement).first()
        if conta_saida.valor < transfered_ammount :
            raise ValueError('Saldo indisponível')
        statement = select(Conta).where(Conta.id==id_destino)
        conta_destino = session.exec(statement).first()
        conta_saida.valor -= transfered_ammount
        conta_destino.valor += transfered_ammount
        session.commit()

def movimentar_dinheiro (historico: Historico):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==historico.conta_id)
        conta = session.exec(statement).first()
        #TO-DO:validar se a conta está ativa
        if historico.tipo == Tipos.ENTRADA:
            conta.valor += historico.dalor
        else:
            if conta.valor < historico.dalor:
                raise ValueError('Saldo insuficiente')
            conta.valor -= historico.dalor

        session.add(historico)
        session.commit()
        return historico
    
def total_contas ():
    with Session(engine) as session:
        statement = select(Conta)
        contas = session.exec(statement).all()
    total = 0
    for conta in contas:
        total +=conta.valor
    return float(total)

def buscar_historicos_entre_datas(data_inicio: date, data_fim: date):
    with Session(engine) as session:
        statement = select(Historico).where(
            Historico.data>=data_inicio,
            Historico.data<=data_fim
        )
        resultados = session.exec(statement).all()
        return resultados
    
def criar_grafico_por_conta():
    with Session(engine) as session:
        statement = select(Conta).where(Conta.status==Status.ATIVO)
        contas = session.exec(statement).all()
        bancos = [i.banco.value for i in contas]
        total = [i.valor for i in contas]
        print (total)
        print (contas)
        import matplotlib.pyplot as plt
        plt.bar(bancos,total)
        plt.show()
