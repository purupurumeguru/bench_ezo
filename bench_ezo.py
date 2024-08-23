from llama_cpp import Llama

def bench_hello(prompt="こんにちは！",
                num_iteration=10, max_tokens=200, filename="bench_hello_result.md"):
    model_data = [
        ("mradermacher/Llama-3.1-8B-EZO-1.1-it-GGUF", "Llama-3.1-8B-EZO-1.1-it.f16.gguf"),
        ("mradermacher/EZO-Common-9B-gemma-2-it-GGUF", "EZO-Common-9B-gemma-2-it.f16.gguf"),
    ]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("## Prompt setting\n\n")
        f.write(f"Prompt: {prompt}\n\n")

        for repo, model_filename in model_data:
            f.write("### Model\n\n")
            f.write(f"* Repository: {repo}\n")
            f.write(f"* Filename: `{model_filename}`\n\n")

            print(f"Processing {repo}, {model_filename}")
            llm = Llama.from_pretrained(
                repo_id=repo,
                filename=model_filename,
                verbose=False
            )

            for i in range(num_iteration):
                out = llm(prompt, max_tokens=max_tokens)
                response = out["choices"][0]["text"].strip()

                f.write(f"### Iteration {i + 1}\n\n")
                f.write("```\n")
                f.write(f"User: {prompt}\n")
                f.write(f"Assistant: {response}\n")
                f.write("```\n\n")

                print(f"Completed iteration {i + 1}")

            f.write("---\n\n")  # Separator between models

    print(f"Benchmark results saved to {filename}")


def bench_hello_with_system_prompt(prompt="こんにちは！", system_prompt="あなたは親切で効率的な日本語AIアシスタントとして、ユーザーの質問に対して丁寧かつ簡潔に回答し、必要に応じて適切なサポートを提供してください。",
                                   num_iteration=10, max_tokens=200, filename="bench_hello_with_system_prompt_result.md"):
    model_data = [
        ("mradermacher/Llama-3.1-8B-EZO-1.1-it-GGUF", "Llama-3.1-8B-EZO-1.1-it.f16.gguf"),
        ("mradermacher/EZO-Common-9B-gemma-2-it-GGUF", "EZO-Common-9B-gemma-2-it.f16.gguf"),
    ]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("## Prompt setting\n\n")
        f.write(f"System prompt: {system_prompt}\n\n")
        f.write(f"Prompt: {prompt}\n\n")


        repo, model_filename = model_data[0]

        f.write("### Model\n\n")
        f.write(f"* Repository: {repo}\n")
        f.write(f"* Filename: `{model_filename}`\n\n")

        print(f"Processing {repo}, {model_filename}")

        llm = Llama.from_pretrained(
            repo_id=repo,
            filename=model_filename,
            verbose=False
        )

        for i in range(num_iteration):
            out = llm.create_chat_completion(
                max_tokens = max_tokens,
                messages = [
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            response = out["choices"][0]["message"]["content"].strip()
            f.write(f"### Iteration {i + 1}\n\n")
            f.write("```\n")
            f.write(f"User: {prompt}\n")
            f.write(f"Assistant: {response}\n")
            f.write("```\n\n")
            print(f"Completed iteration {i + 1}")

        f.write("---\n\n")  # Separator between models

        repo, model_filename = model_data[1]
        f.write("### Model\n\n")
        f.write(f"* Repository: {repo}\n")
        f.write(f"* Filename: `{model_filename}`\n\n")

        print(f"Processing {repo}, {model_filename}")
        llm = Llama.from_pretrained(
            repo_id=repo,
            filename=model_filename,
            verbose=False
        )
        prompt = f"{system_prompt}\n\n{prompt}\n\n"
        for i in range(num_iteration):
            out = llm(prompt, max_tokens=max_tokens)
            response = out["choices"][0]["text"].strip()

            f.write(f"### Iteration {i + 1}\n\n")
            f.write("```\n")
            f.write(f"User: {prompt}\n")
            f.write(f"Assistant: {response}\n")
            f.write("```\n\n")

            print(f"Completed iteration {i + 1}")

        f.write("---\n\n")  # Separator between models

    print(f"Benchmark results saved to {filename}")

if __name__ == "__main__":
    bench_hello()
    bench_hello_with_system_prompt()

    prompts = [
        "二泊三日の北海道旅行のプランを考えてください。",
        "親子丼の作り方をおしえてください。",
        "初詣で神社に行く際のマナーを教えてください。",        
        "五・七・五の俳句を一つ作ってください。",        
    ]

    filenames = [
        "hokkaido_travel",
        "oyakodon_recipe",
        "shrine_etiquette",        
        "haiku_composition",        
    ]

    for prompt, filename in zip(prompts, filenames):
        bench_hello(prompt=prompt, num_iteration=1, max_tokens=2000, filename=f"{filename}_result.md")
        bench_hello_with_system_prompt(prompt=prompt, num_iteration=1, max_tokens=2000, filename=f"{filename}_with_system_prompt_result.md")
