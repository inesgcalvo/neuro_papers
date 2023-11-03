import asyncio


def asincrono(funcion):

    def eventos(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, funcion, *args, **kwargs)
    
    return eventos