
import sys
import os
from instructions import *


def bin_to_hex(bin: str) -> str:
    return hex(int(bin, base=2))[2:]

def is_code_line(line: str) -> bool:
    return len(line) > 0 and (not line.isspace())  and line[0] != '#'

def split_line(line: str):
    sp = line.split()
    if len(sp) != 3:
        raise Exception('line "{}" does not split into 3 parts!'.format(line))
    return (sp[0], sp[1], sp[2])

def translate_part(p: str, di) -> str:
    try:
        re = di[p]
        return re
    except:
        raise Exception('wrong instruction: "{}"'.format(p))

def translate_line(line: str) -> str:
    if not is_code_line(line): return None

    (inp, op, outp) = split_line(line)
    inp  = translate_part(inp, input_commands)
    op   = translate_part(op, operator_commands)
    outp = translate_part(outp, output_commands)

    binary = inp + outp + '000' + op
    print ("binary = {}".format(binary))
    
    he = bin_to_hex(binary)
    print ('hex = {}'.format(he))

    return he

def assemble_file(path: str) -> list:
    if not os.path.isfile(path):
        raise Exception('file "{}" does not exist!'.format(path))

    file = open(path, 'r')
    lines = []
    for line in file:
        translated = translate_line(line)
        if translated is None: continue
        
        lines.append(translated)
    
    return lines

def write_lines(path: str, lines: list):
    file = open(path, 'w+')
    file.write('v2.0 raw\n')

    print("lines={}".format(lines))

    i = 0
    while True:
        for k in range(4):
            if i >= len(lines): 
                file.write('\n')
                file.close()
                return
            
            file.write(lines[i] + ' ')
            
            i += 1
        
        file.write('\n')

if __name__ == "__main__":
    
    lines = assemble_file(sys.argv[1])
    write_lines("code2.tsv", lines)

    print ("\nEND")
