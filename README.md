# 概要

EZOモデルの簡単な評価

# インストールと使用方法

```
git clone https://github.com/purupurumeguru/ezo-bench.git
cd ezo-bench
pip install -r requirements.txt
python bench_ezo.py
```

# 結果

## 「こんにちは！」に対する回答

### システムプロンプトなし
- [こんにちは！](bench_hello_result.md)
- Llama-3.1-8B-EZO-1.1-it
    - 2/10で日本語の返答
    - ブログ記事みたいな内容を出力
- EZO-Common-9B-gemma-2-it
    - 10/10で日本語の返答
    - Llamaの時と同様にブログ記事みたいな内容を出力
- 訓練データに「こんにちは！」から始まるブログのデータがそこそこあるのかも？    

### システムプロンプトあり
```
system_prompt = "あなたは親切で効率的な日本語AIアシスタントとして、ユーザーの質問に対して丁寧かつ簡潔に回答し、必要に応じて適切なサポートを提供してください。"
```
- [こんにちは！（システムプロンプト付き）](bench_hello_with_system_prompt_result.md)
- Llama-3.1-8B-EZO-1.1-it
    - 10/10で日本語の返答
    - AIアシスタントとしてふるまってくれる
    - ちゃんと「こんにちは！」と返事をしてくれる    
    - 「どういたまのご質問」とよく言う
    
- EZO-Common-9B-gemma-2-it
    - 10/10で日本語の返答
    - Llamaと同様にAIアシスタントとしてふるまってくれる
    - 「こんにちは！」と返事をしない    

## その他のプロンプト
- [北海道旅行プラン](hokkaido_travel_result.md)
- [北海道旅行プラン（システムプロンプト付き）](hokkaido_travel_with_system_prompt_result.md)
- [親子丼レシピ](oyakodon_recipe_result.md)
- [親子丼レシピ（システムプロンプト付き）](oyakodon_recipe_with_system_prompt_result.md)
- [神社参拝マナー](shrine_etiquette_result.md)
- [神社参拝マナー（システムプロンプト付き）](shrine_etiquette_with_system_prompt_result.md)
- [俳句作成](haiku_composition_result.md)
- [俳句作成（システムプロンプト付き）](haiku_composition_with_system_prompt_result.md)
