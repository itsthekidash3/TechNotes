AI 

 Transformer architecture (2017).
Tokenization: The Currency of AI
LLMs are stateless

1. Tokenize:
		text is broken into small units and converted into vectors
		text -> token -> id -> vector
		order matters
  2. Attention :
		Each token computes a relevance score against each token, assigns weights
		and blends their information
  3. Compute:
		next token probabilities
		Reasoning emerges from repeated transformations not logic rules
		a) apply transformer layer: Attention + feedforward layers
		b) build contextual understanding : kinda like its value in the sentence
		c) output probabilities
  4. Sampling
  		selects a  next token from probability distribution
  5. Repeat

Context Window : What’s on the Desk
Cost : per token
Limits : context window
Speed : more tokens - slower response
Multilingual: only English

Cosine similarity




The code:

import anthropic                              # pip install anthropic

client = anthropic.Anthropic()                 # uses ANTHROPIC_API_KEY env var

response = client.messages.create(             # send request → get response
    model='claude-sonnet-4-20250514',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': 'What is machine learning?'}
    ]
)

print(response.content[0].text)               


Wanna make a good deicison



A good Prompt :

A) Role
B) Context
C) Task D) Constraints E) Format
F) User Message and System Message

RAG:

An informational Retrieval Problem

1. Query : user input
2. Embed : convert query to vector
3. Search: Find similar chunks : Deterministic
4. Augment: Inject into prompt : Dterministic, top matching chunks
5. Generate: Probabilistic


Memory:

1. Conversation Buffer : Append History
2. Summary : kind of caching and compress
3. Vector Recall : Embedded and store as vectors. Relevant paths
4. Structured: facts from conversations stored in database: Most complex
  “ Logic execution with code “  The model requests. You execute. That's the safety boundary.


Define tools with JSON schema
Pass tools to the API



AI Systems Design Patterns:

Answer Question about data : RAG + chat
Have a conversation : Memory + Chat
Generate Content : Prompting + Structured Output

Tools use : Let AI take action
Agents : Multi-step Automation
Multimodal : Analyze images/Docs





