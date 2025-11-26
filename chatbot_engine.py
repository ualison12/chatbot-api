import datetime
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
                    "Olá! 😄 Em que posso te ajudar?",
                    "Fala! Tô aqui pra te ajudar com Python, projetos e o que mais precisar."
                ]
            },
            "despedida": {
                "padroes": ["tchau", "valeu", "obrigado", "obrigada", "ate mais", "falou"],
                "respostas": [
                    "Valeu! Qualquer coisa é só chamar ✌️",
                    "Até mais! Bons códigos pra você!",
                    "Tchau! Foi bom conversar com você 😄"
                ]
            },
            "duvida_python": {
                "padroes": ["python", "programacao", "codigo", "programar", "script"],
                "respostas": [
                    "Você quer ajuda com lógica, sintaxe ou algum projeto específico em Python?",
                    "Python é ótimo! Me conta melhor qual é a sua dúvida.",
                    "Me fala qual parte de Python você quer aprender: dados, web, automação, IA...?"
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
                    "Eu ia te contar uma piada de UDP, mas talvez você não receba... 😅",
                    "Qual o cúmulo do programador? Ir ao zoológico e ficar debugando o macaco 🐒"
                ]
            },
            "ajuda_geral": {
                "padroes": ["ajuda", "me ajuda", "socorro", "nao sei", "to perdido", "to perdida"],
                "respostas": [
                    "Calma, respira 😄 Me explica com suas palavras o que você quer fazer.",
                    "Tô aqui pra te ajudar. Me conta o problema que você quer resolver.",
                    "Beleza, vamos por partes. O que você está tentando fazer agora?"
                ]
            }
        }

    def _intencao_hora_atual(self) -> str:
        agora = datetime.datetime.now()
        hora_formatada = agora.strftime("%H:%M")
        return f"Agora são {hora_formatada} ⏰"

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
                "Não entendi muito bem 🤔 "
                "Tenta me explicar de outro jeito ou me fala se é sobre Python, carreira, estudos ou outra coisa."
            )

        if intencao == "hora_atual":
            return self._intencao_hora_atual()

        respostas = self.intencoes[intencao]["respostas"]
        return random.choice(respostas)
