import streamlit as st

from agents.analista_vendas_agent import AgenteAnalistaVendas

# Configurar página
st.set_page_config(
    page_title="Analista de Vendas",
    page_icon="💰",
    layout="wide"
)


# Inicializar analista (cache para evitar recriar)
@st.cache_resource
def get_analista():
    return AgenteAnalistaVendas()


def chat():
    # Título e descrição
    st.title("💰 Analista de Vendas")
    st.markdown("*Faça perguntas sobre dados de vendas*")

    # Sidebar com controles
    with st.sidebar:
        st.header("🔧 Controles")
        if st.button("🗑️ Limpar Conversa"):
            st.session_state.messages = [
                {"role": "assistant", "content": "Conversa limpa! Em que posso ajudar?"}
            ]
            st.rerun()

        # Mostrar quantidade de mensagens
        if "messages" in st.session_state:
            st.info(f"📊 Total de mensagens: {len(st.session_state.messages)}")

    # Inicializar histórico
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Boa tarde! Sou seu analista de vendas. Posso ajudar com:\n\n"
                           "• Análise de vendas\n"
                           "• Estatísticas gerais\n\n"
                           "Em que posso ajudar?"
            }
        ]

    # Container para mensagens (permite scroll)
    container = st.container()

    with container:
        # Exibir histórico de mensagens
        for i, message in enumerate(st.session_state.messages):
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # Input do usuário (fixo na parte inferior)
    if prompt := st.chat_input("Digite sua pergunta sobre dados de vendas..."):
        # Adicionar pergunta do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Exibir pergunta do usuário
        with st.chat_message("user"):
            st.write(prompt)

        # Processar e exibir resposta
        with st.chat_message("assistant"):
            try:
                # Mostrar indicador de carregamento
                placeholder = st.empty()
                with placeholder.container():
                    st.info("🤖 Analisando dados...")

                # Obter resposta do agente
                analista = get_analista()
                response = analista.input(prompt)

                # Limpar indicador de carregamento
                placeholder.empty()

                # Extrair e exibir resposta
                if hasattr(response, 'result'):
                    resposta = response
                else:
                    resposta = str(response)

                st.write(resposta)

                # Adicionar ao histórico
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": resposta
                })

            except Exception as e:
                placeholder.empty()
                st.error(f"Erro: {str(e)}")

                # Adicionar erro ao histórico
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"Erro: {str(e)}"
                })

        # Auto-scroll para a última mensagem
        st.rerun()


if __name__ == "__main__":
    chat()
