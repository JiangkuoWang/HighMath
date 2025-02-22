import json
import asyncio
import aiohttp
import random
from tqdm import tqdm

# We have provided an API-calling script that eliminates the need for local model deployment, ensuring ease of use.

api_key = ""
input_file = ""
output_file = ""
data_num = 25000
start_num = 0
freq = 3000
target_lang = ""
random.seed(54)
MAX_CONCURRENT_REQUESTS = 5000
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
MAX_RETRIES = 3

timeout = aiohttp.ClientTimeout(total=1500)  # Increase timeout

async def translate_text_async(session, query, pbar, retry_count=0):
    async with semaphore:
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": query},
        ]

        try:
            async with session.post(
                url="https://api.deepseek.com/chat/completions",
                json={"model": "deepseek-chat", "temperature": 1.1, "messages": messages},
                headers={"Authorization": f"Bearer {api_key}"}
            ) as resp:
                if resp.status == 429:
                    if retry_count < MAX_RETRIES:
                        await asyncio.sleep(2 ** retry_count)
                        return await translate_text_async(session, query, pbar, retry_count + 1)
                    else:
                        return "翻译失败: 达到最大重试次数"

                if resp.status != 200:
                    return f"翻译失败: HTTP {resp.status}"

                if resp.headers['Content-Type'] == 'application/json':
                    response_json = await resp.json()
                    translated_text = response_json['choices'][0]['message']['content']
                    return translated_text
                else:
                    text = await resp.text()
                    print(f"Unexpected Content-Type: {resp.headers['Content-Type']}")
                    print(f"Response: {text}")
                    return "翻译失败: 非预期响应格式"

        except asyncio.TimeoutError:
            print("请求超时")
            if retry_count < MAX_RETRIES:
                await asyncio.sleep(2 ** retry_count)
                return await translate_text_async(session, query, pbar, retry_count + 1)
            else:
                return "翻译失败: 请求超时"
        except aiohttp.ClientError as e:
            print(f"网络错误: {e}")
            if retry_count < MAX_RETRIES:
                await asyncio.sleep(2 ** retry_count)
                return await translate_text_async(session, query, pbar, retry_count + 1)
            else:
                return "翻译失败: 请求处理错误"
        finally:
            pbar.update(1)

async def main():
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []
        translated_results = []

        # with open(input_file, 'r', encoding='utf-8') as file:
        #     data = json.load(file)
        #     data = data[start_num:data_num]

# 读取 JSON 文件
        with open(input_file, 'r', encoding='utf-8') as file:
            # data = json.load(file)
            data = []
            for line in file:
                data.append(json.loads(line))
            data = data[:data_num]


        with tqdm(total=len(data) * 2, desc="Translating", unit="item") as pbar:
            for idx, item in enumerate(data):
                query = item.get('query', '')
                query = f"Please translate the following sentences into {target_lang}: \"{query}\""
                response = item.get('response', '')
                response = f"Please translate the following sentences into {target_lang}: \"{response}\""

                tasks.append(translate_text_async(session, query, pbar))
                tasks.append(translate_text_async(session, response, pbar))

                if (idx + 1) % freq == 0:
                    translated_texts = await asyncio.gather(*tasks)
                    tasks = []

                    for i in range(0, len(translated_texts), 2):
                        translated_results.append({
                            'query': translated_texts[i],
                            'response': translated_texts[i+1],
                        })

                    # for i in range(0, len(translated_texts), 1):
                    #     translated_results.append({
                    #         'query': translated_texts[i],
        
                    #     })

                    with open(output_file, 'a', encoding='utf-8') as output_files:
                        for result in translated_results:
                            output_files.write(json.dumps(result, ensure_ascii=False, indent=4) + '\n')
                    translated_results = []

            if tasks:
                translated_texts = await asyncio.gather(*tasks)
                for i in range(0, len(translated_texts), 2):
                    translated_results.append({
                        'query': translated_texts[i],
                        'response': translated_texts[i+1],
                    })

                with open(output_file, 'a', encoding='utf-8') as output_files:
                    for result in translated_results:
                        output_files.write(json.dumps(result, ensure_ascii=False, indent=4) + '\n')

        print(f"finished, saved in {output_file} ")

asyncio.run(main())