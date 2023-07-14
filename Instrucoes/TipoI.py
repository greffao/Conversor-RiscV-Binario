# Classe Tipo I
from Instrucoes.Instrucao import Instrucao

opcodes = { 
    "jalr" : "1100111",
    "lb"   : "0000011",
    "lh"   : "0000011",
    "lw"   : "0000011",
    "lbu"  : "0000011",
    "lhu"  : "0000011",
    "addi" : "0010011",
    "slti" : "0010011",
    "sltiu": "0010011",
    "xori" : "0010011",
    "ori"  : "0010011",
    "andi" : "0010011"
}

functs3 = {
    "jalr" : "000",
    "lb"   : "000",
    "lh"   : "001",
    "lw"   : "010",
    "lbu"  : "100",
    "lhu"  : "101",
    "addi" : "000",
    "slti" : "010",
    "sltiu": "011",
    "xori" : "100",
    "ori"  : "110",
    "andi" : "111"
}

class TipoI(Instrucao):
    def __init__(self, texto):
        super().__init__(texto)

        self.mneumonico = super().get_mnemonico()
        self.rd_nome = super().get_primeiro_reg()

        if(self.mneumonico[0] == 'l'):
            self.rs1_nome = super().get_base_reg()
            self.imm = super().get_offset()
        else:
            self.rs1_nome = super().get_segundo_reg()
            self.imm = super().get_imm_ou_reg()

        if(not ((self.imm).isdigit())):
            raise TypeError("Esperado um valor imediato inteiro!")
        
        if(int(self.imm) > 4095 or int(self.imm) < -4095):
            raise ValueError("Esperado um valor que pode ser representado com 12 bits!")


    def get_registradores(self):
        # Conversao do registrador destido (rd)
        rd = super().regParaBin(self.rd_nome)

        # Conversao do registrador origem 1 (rs1)
        rs1 = super().regParaBin(self.rs1_nome)

        return (rd, rs1)
    
    def get_imediato(self):
        # Convertendo o valor imediato para binário
        return bin(int(self.imm))[2:].zfill(12)

    def __str__(self):
        rd, rs1 = self.get_registradores()

        opcode = opcodes[self.mneumonico]

        funct3 = functs3[self.mneumonico]

        imm = self.get_imediato()

        codigo_inteiro = f'{imm} {rs1} {funct3} {rd} {opcode}'

        return ('opcode: ' + opcode + '\n' +
                'rd: ' + rd + '\n' +
                'funct3: '+ funct3 + '\n' +
                'rs1: ' + rs1 + '\n' +
                'imm: ' + imm + '\n\n' +
                'Binário: ' + codigo_inteiro + '\n')
