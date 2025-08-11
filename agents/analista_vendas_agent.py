from langchain_ollama import OllamaLLM

from tools.ler_documentos_tool import LerDocumentos


class AgenteAnalistaVendas:
    def __init__(self):
        self.llm = OllamaLLM(
            model="llama3.1",
            # base_url="http://localhost:11434", # Executar na IDE
            base_url="http://accenture-challenge-ollama:11434", # Executar na Docker
            temperature=0.1,
        )
        self.ler_documentos = LerDocumentos()

    def input(self, prompt):
        ler_documentos = LerDocumentos()
        print(f"Entrada: {prompt}")
        output = ler_documentos.output(self.llm, prompt)
        print(f"Saída..: {output}")
        return output['result']