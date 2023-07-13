# Classe tipo R
from Instrucao import Instrucao


class TipoR(Instrucao):
    def __init__(self, texto):
        super().__init__(texto)

    def converter(self):
        instrucao = self.instrucao
        opcode = ''
        funct3 = ''
        funct7 = ''
        rd = 'ERRO'
        rs1 = 'ERRO'
        rs2 = 'ERRO'


        # Conersao do registrador destido (rd)
        a = 0  # Quantidade de caracteres necessarios para ler corretamente
        registador = instrucao[4:8]
        if(registador[-2] == ','):
            rd = super().regParaBin((registador[0:2]))
        elif(registador[-1] == ',' and rd == 'ERRO'):
            rd = super().regParaBin((registador[0:3]))
            a += 1
        elif(rd == 'ERRO'):
            rd = super().regParaBin('zero')
            a += 1


        # Conversao do regristrador origem 1 (rs1)
        b = 0  # Quantidade de caracteres necessarios para ler corretamente
        registador = instrucao[8 + a:12 + a]
        if (registador[-2] == ','):
            rs1 = super().regParaBin((registador[0:2]))
        elif (registador[-1] == ',' and rs1 == 'ERRO'):
            rs1 = super().regParaBin((registador[0:3]))
            b += 1
        elif (rs1 == 'ERRO'):
            rs1 = super().regParaBin('zero')
            b += 1

        # Conversao do regristrador origem 2 (rs2)
        registador = instrucao[12 + a + b:]
        rs2 = super().regParaBin((registador))

        if(instrucao[:3] == 'add'):
            opcode = '0110011'
            funct3 = '000'
            funct7 = '0000000'
        elif(instrucao[:3] == 'sub'):
            opcode = '0110011'
            funct3 = '000'
            funct7 = '0100000'
        elif(instrucao[:3] == 'and'):
            opcode = '0110011'
            funct3 = '111'
            funct7 = '0000000'


        codigo_inteiro = opcode + ' ' + rd + ' ' + funct3 + ' ' + rs1 + ' ' + rs2 + ' ' + funct7
        return ('opcode: ' + opcode + '\n' +
                'rd: ' + rd + '\n' +
                'funct3: '+ funct3 + '\n' +
                'rs1: ' + rs1 + '\n' +
                'rs2: ' + rs2 + '\n' +
                'funct7: ' + funct7 + '\n\n' +
                'Código Inteiro: ' + codigo_inteiro + '\n')