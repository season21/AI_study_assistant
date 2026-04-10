from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text2text-generation",
    temperature=0.7,
    max_new_tokens=300
)

#model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

# Prompt Templates
notes_prompt = PromptTemplate(
    template="Generate clear study notes for the following topic:\n{topic}",
    input_variables=["topic"]
)

quiz_prompt = PromptTemplate(
    template="Generate 5 quiz questions from this topic:\n{topic}",
    input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template="Give a short summary of the topic:\n{topic}",
    input_variables=["topic"]
)

# Chains
notes_chain = notes_prompt | llm | parser
quiz_chain = quiz_prompt | llm | parser
summary_chain = summary_prompt | llm | parser

# Parallel Chain
study_chain = RunnableParallel(
    notes=notes_chain,
    quiz=quiz_chain,
    summary=summary_chain
)

#invoke function
#result = study_chain.invoke({"topic"})