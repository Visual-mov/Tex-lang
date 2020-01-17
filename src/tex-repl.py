import re, sys
from parse.parser import Parser
from parse.tokenizer import Tokenizer
import eval.evaluator as eval

# The Tex Programming Language
# www.github.com/Visual-mov/Tex-lang
#
# Copywrite(c) Ryan Danver (Visual-mov) 2019

def repl(argv):
    run = True
    gScope = eval.Scope("Global")

    if len(argv)-1 > 1 and argv[1] == "--file":
        try: source = open(argv[2],'r').read()
        except FileNotFoundError:
            repl_error(f"Can not find file: \"{argv[2]}\"")
        tokenizer = Tokenizer(source)
        tokens = tokenizer.lex()
        tokenizer.print_tokens()

        ast = Parser(tokens).parse()
        print(str(ast) + '\n')
        
        evaluator = eval.Evaluator(ast, gScope)
        evaluator.eval()
    else:
        print("Tex Language REPL\nCreated by Ryan Danver 2019")
        line = 1
        while run:
            try: eval.Evaluator(Parser(Tokenizer(input(">> ").replace('\n',''), line).lex()).parse(),gScope).eval()
            except KeyboardInterrupt:
                repl_error()
            line += 1

def repl_error(message=""):
    print(message)
    exit()

if __name__ == "__main__":
    repl(sys.argv)