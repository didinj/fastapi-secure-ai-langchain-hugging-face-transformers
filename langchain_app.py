# langchain_app.py
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

# Load tokenizer and model (you can replace 'gpt2' with any model you prefer)
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Create the pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=100)

# Wrap with LangChain
llm = HuggingFacePipeline(pipeline=generator)

# Optional: Add prompt template
template = PromptTemplate(
    input_variables=["prompt"],
    template="Answer the following: {prompt}"
)

llm_chain = LLMChain(prompt=template, llm=llm)

def generate_response(prompt: str) -> str:
    result = llm_chain.run(prompt)
    return result.strip()
