import guidance
from guidance import select, gen
from ..utils import get_model

def test_llama_cpp_gen():
    lm = get_model("llama_cpp:")
    lm = lm + "this is a test" + gen("test", max_tokens=10)
    assert len(str(lm)) > len("this is a test")

def test_llama_cpp_recursion_error():
    lm = get_model("llama_cpp:")

    # define a guidance program that adapts a proverb
    lm = lm + f"""Tweak this proverb to apply to model instructions instead.
    {gen('verse', max_tokens=2)}
    """
    assert len(str(lm)) > len("Tweak this proverb to apply to model instructions instead.\n\n")

def test_llama_cpp_select2():
    lm = get_model("llama_cpp:")
    lm += f'this is a test1 {select(["item1", "item2"])} and test2 {select(["item3", "item4"])}'
    assert str(lm) in [
        "this is a test1 item1 and test2 item3", 
        "this is a test1 item1 and test2 item4",
        "this is a test1 item2 and test2 item3", 
        "this is a test1 item2 and test2 item4"]

