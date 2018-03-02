with open('tmp/index.html') as f:
    index = f.read()

with open('tmp/index.html'):
    print('great')

with A() as X, B() as Y, C() as Z:
    do_something()

with A() as X:
    with B() as Y:
        with C() as Z:
            do_something()

with long_context_manager_1_aaaaaa, long_context_manager_1_aaaaaa, long_context_manager_1_aaaaaa: pass

with long_context_manager_1_aaaaaa, long_context_manager_1_aaaaaa: long_function_name()
