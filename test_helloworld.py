from helloworld import say_hello

def test_helloworld_no_args():
    assert say_hello() == "Hello, World!"

def test_helloworld_with_args():
    assert say_hello("Everyone") == "Hello, Everyone!"
