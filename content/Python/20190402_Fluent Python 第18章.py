# Fluent Python 18章 asyncioによる並行処理を Python 3.7で実装します。 [公式の
# HP](https://github.com/fluentpython/example-code)にもPython 3.7用のアップデートがあり
# ます。

# ## スレッドとコルーチン

# 以下の例では、Jupyter clientで実行できるように、
# [nest_asyncio](https://github.com/erdewit/nest_asyncio)パッケージを使っています。

# #例 18.2
import asyncio
import itertools
import sys

import nest_asyncio

nest_asyncio.apply()


async def spin():
    for char in itertools.cycle("|/-\\"):
        sys.stdout.write(char)
        sys.stdout.flush()
        try:
            await asyncio.sleep(0.5)
        except asyncio.CancelledError:
            break


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin())
    print("spinner object:", spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    coro = supervisor()
    result = asyncio.run(coro)
    print("Answer:", result)


if __name__ == "__main__":
    main()
