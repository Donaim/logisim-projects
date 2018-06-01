
import sys
import os
from instructions import *

def bin_to_hex(bin: str) -> str:
    return hex(int(bin, base=2))[2:]

def is_code_line(line: str) -> bool:
    return len(line) > 0 and (not line.isspace())  and line[0] != '#'

def pad_args(args: list):
    for i in range(len(args), 3):
        args.append('%')

def isnumber(string: str):
    try:
        f = int(string)
        return True
    except:
        return False
def ischar(string: str):
    l = len(string)
    if l < 3: 
        return False
    if string[0] != "\'" or string[-1] != '\'':
        return False
    if l > 4: 
        return False
    if l == 4 and string[1] != '\\':
        return False
    return True

def split_line(line: str):
    (line, _, _) = line.partition('#')
    (out, _, com) = line.partition('=')
    out = out.strip()
    com = com.strip()

    if len(com) == 0:
        raise Exception('command in line "{}" cannot be empty!'.format(line))

    csp = com.split()
    csp = list(map (str.strip, csp))

    op = csp[0]
    if not op in operators: # if not operator, then maybe input
        if isnumber(com):
            return ((out, com), "number")
        elif ischar(com):
            com = convert_char_to_decimal(com)
            return ((out, com), "number")
        else:
            csp = ['x', op]
            op = csp[0]
    args = csp[1:]

    need_args_count = translate_part(op, operators)[1]
    curr_args_count = len(args)

    if curr_args_count != need_args_count:
        raise Exception("operation {} expects {} arguments but {} were given".format(op, need_args_count, curr_args_count))

    pad_args(args)

    return ((out, op, args[0], args[1], args[2]), "expr")

def translate_part(p: str, di) -> str:
    try: return di[p]
    except: raise Exception('wrong instruction: "{}"'.format(p))

def convert_decimal_to_binary(dec: str) -> str:
    s =  bin( int(dec) )[2:]
    if len(s) > 20: 
        raise Exception('number {} is greater than 20 bits which is not supported'.format(dec))
    zeros = "0" * (20 - len(s))
    s = zeros + s
    return s
def convert_char_to_decimal(ch: str) -> str:
    ch = ch.strip("\'")
    if ch == "\\n":
        ch = '\n'
    elif ch == "\\t":
        ch = '\t'
    return str(ord(ch))

def get_literal_command_binary(vs: list) -> str:
    (outp, num) = vs
    
    outp = translate_part(outp, output_adresses)
    numb = convert_decimal_to_binary(num)

    binary = outp + numb
    # print ("binary = {}".format(binary))
    return binary

def get_normal_command_binary(vs: list) -> str:
    (outp, op, x, y, z) = vs

    # print ("splitted={}".format([outp, op, x, y, z]))

    outp = translate_part(outp, output_adresses)
    op   = translate_part(op, operators)[0]
    x    = translate_part(x, input_adresses)
    y    = translate_part(y, input_adresses)
    z    = translate_part(z, input_adresses)
    # print ("binary splitted={}".format([x, y, z, outp, op]))

    binary = outp + '100' + op + x + y + z
    # print ("binary = {}".format(binary))
    return binary
def get_binary_from_line(vs: list, rtype) -> str:
    if rtype == 'expr':
        return get_normal_command_binary(vs)
    if rtype == 'number':
        return get_literal_command_binary(vs)
    raise NotImplementedError('unknown rtype: {}'.format(rtype))
def translate_line(line: str) -> str:
    if not is_code_line(line): return None

    (vs, rtype) = split_line(line)
    binary = get_binary_from_line(vs, rtype)
    return bin_to_hex(binary)

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

    print("\nlines={}".format(lines))

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
    print("")
    
    lines = assemble_file(sys.argv[1])
    output =  sys.argv[2] if len(sys.argv) > 2 else 'a.out' 
    write_lines(output, lines)

    print ("\nEND")
