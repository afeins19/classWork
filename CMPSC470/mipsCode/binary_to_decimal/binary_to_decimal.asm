.data
result: .space 32  # make space for output
user_prompt_str: .asciiz "\n[Program by Aaron Feinberg]\n\nPlease Input a Base 10 Value:\n"
result_prompt_str: .asciiz "\nYour Value in Base 2 is:\n"
bin_val_str: .space 32  # will hold the binary value string

.text
greeting:
    # greets the user and prompts them to enter a value in base 10
    li $v0, 4
    la $a0, user_prompt_str
    syscall

main:
    # getting user's value after greeting
    li $v0, 5
    syscall

    move $a0, $v0  # moving user val to $a0

    # Declare register vals
    li $t0, 0          # bit counter
    li $v0, 0          # store the binary result (init to 0)

bin_loop:
    beq $a0, 0, print_results  # if we shifted $a0 all the way, exit

    # Get the LSB and add it to $v0, shifted left by $t0 bits
    andi $t1, $a0, 1   # isolate LSB
    sllv $t1, $t1, $t0  # shift LSB left by $t0 bits
    or $v0, $v0, $t1   # add the shifted bit to $v0

    # Prepare for the next iteration
    srl $a0, $a0, 1   # shift all bits in $a0 right
    addi $t0, $t0, 1   # increment bit counter
    j bin_loop

print_results:
    # Converting binary value to string for printing
    li $t1, 31  # 32 bits allocated to the results so we count 31->0
    la $t2, bin_val_str  # set $t2 to address of bin_val_str

str_loop:
    srlv $t3, $v0, $t1   # shift $v0 right by $t1 bits
    andi $t3, $t3, 1     # isolate the LSB
    addi $t3, $t3, 48    # convert to ASCII (0->48, 1->49)
    sb $t3, 0($t2)       # store the byte (0 or 1) in t3 into the address given by t2
    addi $t2, $t2, 1     # increment t2 to grab address of next byte
    addi $t1, $t1, -1    # decrement bit counter
    bgez $t1, str_loop   # if $t1 >= 0, jump to str_loop and loop again

    sb $zero, 0($t2)     # null terminate the string

    # Print output
    li $v0, 4
    la $a0, result_prompt_str
    syscall

    li $v0, 4
    la $a0, bin_val_str
    syscall

    li $v0, 10  # exit
    syscall
