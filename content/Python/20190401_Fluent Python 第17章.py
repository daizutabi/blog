# 「Fluent Python 17章 futuresを使った並行処理」をPython 3.7で実装します。 [公式の
# HP](https://github.com/fluentpython/example-code)にもPython 3.7用のアップデートがあり
# ます。

# ## 逐次型ダウンロードスクリプト

# #例 17.1 共通項目
# -run
import asyncio
import sys
import time
from concurrent import futures

import aiohttp
import nest_asyncio
import requests

nest_asyncio.apply()

POP20_CC = ("CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR").split()

BASE_URL = "http://flupy.org/data/flags"


def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    sys.stdout.write(text + " ")
    sys.stdout.flush()


def main(func):
    t0 = time.time()
    count = func(POP20_CC)
    elapsed = time.time() - t0
    msg = "\n{} flags downloaded in {:.2f}s"
    print(msg.format(count, elapsed))


# #例 17.2 flags.py
def download_many(cc_list):
    for cc in sorted(cc_list):
        get_flag(cc)
        show(cc)

    return len(cc_list)


if __name__ == "__main__":
    main(download_many)


# ## concurrent.futuresを使ったダウンロードスクリプト

# #例 17.3 flags_threadpool.py
MAX_WORKERS = 20


def download_one(cc):
    get_flag(cc)
    show(cc)
    return cc


def download_many_threadpool(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))


if __name__ == "__main__":
    main(download_many_threadpool)


# #例 17.4 flags_threadpool_ac.py
def download_many_threadpool_ac(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = "Scheduled for {}: {}"
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = "{} result: {!r}"
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == "__main__":
    main(download_many_threadpool_ac)


# ## asyncio/aiohttpを使ったダウンロードスクリプト

# #例 17.5 flags_asyncio.py
async def get_flag_async(session, cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    async with session.get(url) as resp:
        return await resp.read()


async def download_one_async(session, cc):
    await get_flag_async(session, cc)
    show(cc)
    return cc


async def download_many_async(cc_list):
    async with aiohttp.ClientSession() as session:
        aws = [
            asyncio.create_task(download_one_async(session, cc))
            for cc in sorted(cc_list)
        ]
        res = await asyncio.gather(*aws)

    return len(res)


if __name__ == "__main__":
    main(lambda x: asyncio.run(download_many_async(x)))
