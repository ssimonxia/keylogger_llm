# Keylogger with Large Language Model  
## Overview  
In the digital age, the need for sophisticated tools to monitor and analyze computer activities has become increasingly critical. This project presents the development of an advanced keylogger designed using the Rust programming language, aimed at capturing comprehensive data from computer systems, including file interactions, user actions, and keystrokes. The keylogger incorporates innovative algorithms to filter and highlight potentially sensitive information, thereby minimizing the necessity for exhaustive manual review by unauthorized users. To further obfuscate the collected data from computer owners, encryption and decryption algorithms were implemented, ensuring secure handling and retrieval of the logs. Motivated by recent advancements in large language models (LLMs), the project integrates these models to enhance the analysis of keylogger outputs, providing more nuanced and accurate interpretations of the captured data. This project underscores the significance of leveraging advanced technologies to improve data capture and analysis.

## Run the Code
1. Replace "your openai api key" in `llm.py` with your own OpenAI API key  
2. Run the following commands to run the keylogger  
```bash
   cargo build
   cargo run
```
3. The keylogger log file, the algorithm processed log file, and large language model analysis file will be in `bin`

## Reference
* information about keylogger: https://github.com/thomaslienbacher/win-keylogger-rs.git 
* winapi: https://docs.rs/winapi/latest/winapi/
