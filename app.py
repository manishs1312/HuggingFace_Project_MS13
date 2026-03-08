from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("Artificial Intelligence will change", max_length=50)

print(result)
