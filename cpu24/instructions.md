# SYMBOLS
`CURR`: current output


# OPERATOR

00000:     0x00000
00001:     0xfffff
00010:     A
00011:     B
00100:     C
00101:     ~A               (bitwise negate)
00110:     -A               (arithmetic negate)
00111:     A++
01000:     A == 0
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


# MOD

  000:     HALT
  001:     A = CURR
  010:     B = CURR
  011:     C = CURR
  100:     A = MEM                   (load MEM to A)
  101:     MEM = CURR                (load CURR to MEM)
  110:     NEW_MEM_ADR = CURR
  111:     A <- STEP;   B <-A;   C <- B;   NEXT_STEP = CURR         (jump to line with number CURR)

