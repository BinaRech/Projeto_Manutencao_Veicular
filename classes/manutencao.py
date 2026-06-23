from datetime import datetime, timedelta
from classes.tipo_manutencao import TipoManutencao

class Manutencao:
    def __init__(self, id_manutencao, id_carro, tipo_manutencao, data_manutencao, custo, fornecedor, observacoes=""):
        if not isinstance(tipo_manutencao, TipoManutencao):
            raise TypeError("tipo_manutencao deve ser uma instância de TipoManutencao")

        self.id_manutencao = id_manutencao
        self.id_carro = id_carro
        self.tipo_manutencao = tipo_manutencao
        self.data_manutencao = data_manutencao
        self.custo = custo
        self.fornecedor = fornecedor
        self.observacoes = observacoes
    
    def registrar_manutencao(self):
        """Registra uma nova manutenção"""
        self.data_manutencao = datetime.now()
        return f"Manutenção {self.id_manutencao} registrada em {self.data_manutencao.strftime('%d/%m/%Y %H:%M:%S')}"
    
    def obter_historico(self, historico_completo):
        """Retorna o histórico de manutenções de um veículo"""
        return [m for m in historico_completo if m.id_carro == self.id_carro]
    
    def verificar_proxima_revisao(self, intervalo_dias=None):
        """Verifica a próxima data de revisão recomendada"""
        if intervalo_dias is None:
            if self.tipo_manutencao.periodicidade_meses is not None:
                intervalo_dias = self.tipo_manutencao.periodicidade_meses * 30
            else:
                intervalo_dias = 180

        proxima_revisao = self.data_manutencao + timedelta(days=intervalo_dias)
        dias_restantes = (proxima_revisao - datetime.now()).days
        
        return {
            "data_proxima_revisao": proxima_revisao.strftime('%d/%m/%Y'),
            "dias_restantes": dias_restantes,
            "vencida": dias_restantes < 0,
            "intervalo_dias": intervalo_dias
        }
    
    def exibir_dados(self):
        """Exibe os dados da manutenção"""
        print(f"ID: {self.id_manutencao}")
        print(f"ID Carro: {self.id_carro}")
        print("\nTipo de manutenção: \n")
        print(f"Nome: {self.tipo_manutencao.nome}")
        print(f"Descrição: {self.tipo_manutencao.descricao}")
        if self.tipo_manutencao.periodicidade_meses is not None:
            print(f"Periodicidade: {self.tipo_manutencao.periodicidade_meses} meses")
        print(f"Data: {self.data_manutencao}")
        print(f"Custo: R$ {self.custo:.2f}")
        print(f"Fornecedor: {self.fornecedor}")
        print(f"Observações: {self.observacoes}\n")