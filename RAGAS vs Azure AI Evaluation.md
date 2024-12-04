# RAGAS vs Azure AI Evaluation SDK

Esse documento ajuda a entender um pouco melhor sobre o RAGAS e o Azure AI Evaluation SDK para tomar a decisão de qual seria a melhor ferramenta para utilizarmos.

## RAGAS

### RAGAS Prós

- Processo de Avaliação Simplificado: O RAGAS simplifica o processo de avaliação para pipelines RAG, economizando tempo e recursos.
- Opções de Integração: Oferece opções de integração com várias ferramentas e recursos, como adaptação automática de prompts e geração de dados de teste sintéticos.
- Aplicabilidade Ampla: Suporta uma ampla gama de modelos RAG e sistemas de recuperação, garantindo uma aplicabilidade ampla.
- Avaliação Abrangente: Ao aproveitar um conjunto fornecido de documentos, o RAGAS pode criar um conjunto de dados de avaliação abrangente que cobre vários aspectos de desempenho dos componentes dentro do seu pipeline.

### RAGAS Contras

- Complexidade: Configurar e configurar o RAGAS pode exigir um entendimento mais profundo do framework e de seus componentes.
- Métricas Limitadas: As métricas fornecidas pelo RAGAS podem não cobrir todas as necessidades de avaliação para casos de uso específicos.

## Azure AI Evaluation SDK

### Azure AI Evaluation Prós

- Avaliadores Integrados: O Azure AI Evaluation SDK vem com avaliadores integrados que podem ser usados tanto localmente quanto remotamente na nuvem.
- Integração com Serviços Azure: Integra-se perfeitamente com outros serviços Azure, proporcionando uma experiência unificada para avaliar aplicações de IA.
- Documentação Abrangente: O SDK é bem documentado, facilitando para os desenvolvedores começarem e entenderem suas capacidades.

### Azure AI Evaluation  Contras

- Custo: Executar avaliações usando o Azure AI Evaluation SDK pode incorrer em custos, especialmente ao usar avaliadores baseados em GPT.
- Dependência do Azure: O SDK é fortemente integrado com os serviços Azure, o que pode não ser ideal para usuários que preferem uma solução mais agnóstica em termos de plataforma.

Tanto o RAGAS quanto o Azure AI Evaluation SDK têm seus pontos fortes e fracos, e a escolha entre eles depende de seus requisitos específicos e preferências. Se você precisa de um processo de avaliação simplificado com ampla aplicabilidade, o RAGAS pode ser a melhor escolha. Por outro lado, se você prefere uma solução que se integre perfeitamente com os serviços Azure e forneça avaliadores integrados, o Azure AI Evaluation SDK pode ser mais adequado.

https://learn.microsoft.com/en-us/azure/ai-studio/concepts/evaluation-approach-gen-ai
https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/evaluate-sdk
https://docs.ragas.io/en/v0.1.21/index.html
https://docs.ragas.io/en/v0.1.21/howtos/customisations/azure-openai.html
