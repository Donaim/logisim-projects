# SYMBOLS
`CURR`: current output

# STRUCTURE
4 : INPUT
4 : OUTPUT
3 : NOT USED
5 : OPERATOR INSTRUCTION

# OPERATOR

00000:     0x00000
00001:     0xfffff
00010:     A
00011:     B
00100:     C
00101:     ~A               (bitwise negate)
00110:     -A               (arithmetic negate)
00111:     !A               (boolean negate)
01000:     A++
01001:     #A               (count bits in A)
01010:     A + B
01011:     A - B
01100:     A * B
01101:     A / B
01110:     A % B            (A mod B)
01111:     A & B
10000:     A | B
10001:     A ^ B
10010:     A << B           (A bit shift by B)
10011:     A == B
10100:     A > B
10101:     if A then B else 0
10110:     if A then B else C
10111:     
11000:     
11001:     
11010:     
11011:     
11100:     
11101:     
11110:     
11111:     


# INPUTS
 0000:    operator
 0001:    A
 0010:    B
 0011:    C
 0100:    step
 0101:    mem
 0110:    mem_adr
 0111:    k0
 .....    kn

# OUTPUTS
 0000:    calc
 0001:    new_a
 0010:    new_b
 0011:    new_c
 0100:    next_step
 0101:    new_mem
 0110:    new_mem_adr
 0111:    p0
 .....    pn
