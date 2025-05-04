### Embedding Costs

def print_embedding_cost(texts):
    import tiktoken
    
    enc = tiktoken.encoding_for_model('text-embedding-3-large')
    
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])

    cost = total_tokens / 1000 * 0.00013
    
    print(f"Total Tokens: {total_tokens}")
    print(f"Embedding Cost in USD: ${cost:.6f}")