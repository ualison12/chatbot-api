chatbotimport datetime
import random
import unicodedata


class Chatbot:
    def __init__(self, nome="UaliBot"):
        self.nome = nome
        self._criar_intencoes()

    def _normalizar_texto(self, texto: str) -> str:
        texto = texto.lower()
        texto = unicodedata.normalize("NFD", texto)
        texto = texto.encode("ascii", "ignore").decode("utf-8")
        return texto

    def _criar_intencoes(self):
        self.intencoes = {
            "saudacao": {
                "padroes": ["oi", "ola", "bom dia", "boa tarde", "boa noite", "eai", "fala ai"],
                "respostas": [
                    "Oi! Tudo bem? Como posso te ajudar hoje?",
                    "Ola!  Em que posso te ajudar?",
                    "Fala! To aqui pra te ajudar com Python, projetos e o que mais precisar."
                ]
            },
            "despedida": {
                "padroes": ["tchau", "valeu", "obrigado", "obrigada", "ate mais", "falou"],
                "respostas": 
                [
                    "Valeu! Qualquer coisa e so chamar",
                    "Ate mais! Bons codigos pra voce!",
                    "Tchau! Foi bom conversar com voce"
                ]
            },
            "duvida_python": {
                "padroes": ["python", "programacao", "codigo", "programar", "script"],
                "respostas": [
                    "Voce quer ajuda com logica, sintaxe ou algum projeto especifico em Python?",
                    "Python e otimo! Me conta melhor qual e a sua duvida.",
                    "Me fala qual parte de Python voce quer aprender: dados, web, automação, IA...?"
                ]
            },
            "hora_atual": {
                "padroes": ["hora", "que horas sao", "horario"],
                "respostas": []
            },
            "piada": {
                "padroes": ["piada", "piadinha", "brincadeira", "engracado"],
                "respostas": [
                    "Por que o programador confunde Halloween com Natal? Porque OCT 31 == DEC 25 😂",
                    "Eu ia te contar uma piada de UDP, mas talvez voce nao receba...",
                    "Qual o cumulo do programador? Ir ao zoologico e ficar debugando o macaco 🐒"
                ]
            },
            "ajuda_geral": {
                "padroes": ["ajuda", "me ajuda", "socorro", "nao sei", "to perdido", "to perdida"],
                "respostas": [
                    "Calma, respira Me explica com suas palavras o que voce quer fazer.",
                    "To aqui pra te ajudar. Me conta o problema que voce quer resolver.",
                    "Beleza, vamos por partes. O que voce esta tentando fazer agora?"
                ]
            }
        }

    def _intencao_hora_atual(self) -> str:
        agora = datetime.datetime.now()
        hora_formatada = agora.strftime("%H:%M")
        return f"Agora sao {hora_formatada} "

    def detectar_intencao(self, mensagem: str) -> str:
        texto = self._normalizar_texto(mensagem)
        for nome_intencao, dados in self.intencoes.items():
            for padrao in dados["padroes"]:
                if padrao in texto:
                    return nome_intencao
        return "desconhecida"

    def responder(self, mensagem: str) -> str:
        intencao = self.detectar_intencao(mensagem)

        if intencao == "desconhecida":
            return (
                "Nao entendi muito bem "
                "Tenta me explicar de outro jeito ou me fala se e sobre Python, carreira, estudos ou outra coisa."
            )

        if intencao == "hora_atual":
            return self._intencao_hora_atual()

        respostas = self.intencoes[intencao]["respostas"]
        return random.choice(respostas)
