Demo II -- Game Of Life

Section I

a) check blinker it should show the different state



Underpopulation: A live cell that has < 2 live neighbouring cells will die

Survival: A live cell that has 2-3 live neighbouring cells will remain alive

Overpopulation: A live cell with more than 3 live neighbours will die

Reproduction: A dead cell with exactly 3 live neighbours will become alive

[python - Sum of 8 neighbors in 2d array - Stack Overflow](https://stackoverflow.com/questions/36964875/sum-of-8-neighbors-in-2d-array) 



b) 

just check it , is gliding  

is working? it will go four cycle and diagonaly 

By running test_gameoflife_glider.py



c) 

fix line : self.grid[index[0]+6, index[1]+18] = self.aliveValue

[Gosper glider gun - LifeWiki](https://conwaylife.com/wiki/Gosper_glider_gun)

now to setup the glider gun rle?

https://stackoverflow.com/questions/45577236/game-of-life-rle-format-line-ending-with-number



d) [#413](https://edstem.org/au/courses/22228/discussion/2609614)

get 3 patterns from https://conwaylife.com/wiki/LifeWiki:News_archive

o is alive and - is die 

steps : strip() the strings then skip all the ! 

check for valid characters 

then calculate the dimension, use the longest width 

normalized line by padding dead cells ( because of the longest line)

insert pattern into grid

return value

e) done just add one more pattern more than 20x20



Section II

f) https://www.youtube.com/watch?v=KuXjwB4LzSA

https://www.youtube.com/watch?v=Y03LVHWc6rE

https://www.youtube.com/watch?v=nq78huA2B4c

https://nicholasrui.com/2017/12/18/convolutions-and-the-game-of-life/

https://gist.github.com/mikelane/89c580b7764f04cf73b32bf4e94fd3a3

Problem with method in part a was it uses nested loops to count neighbors, 

resulting in $ O(N^2 \times 8) $ operations per generation, which is inefficient for $ N > 1024 $.

To optimize our problem, we can calculate cells simultaneously using a 2D convolution, 

which is much faster for large grids.

scipy.signal.convolve2d



g) so this part, use the rle.RunLengthEncodedParser to parse the rleString from the RLE.py file

parser.pattern_2d_array gives the 2D pattern as a list of lists with b (dead) and o (live) cells.

this is to get dimension and data

parser.size_x and parser.size_y give the pattern’s dimensions.

then do conversion to - and O 

insert pattern into grid

return value



h) running turing rle with just the implementation in part G.

![image-20250501165946690](C:\Users\brand\AppData\Roaming\Typora\typora-user-images\image-20250501165946690.png)

i) YES

The Game of Life (GoL) is **Turing complete**, meaning it can simulate any computation that a Turing machine can perform

A system is **Turing complete** if it can simulate a **universal Turing machine (UTM)**—a Turing machine capable of simulating any other Turing machine, thus computing any computable function. 

1.Store and manipulate an effectively infinite amount of data (emulating the tape).

2.Implement a finite state machine with arbitrary transition rules.

3.Perform read, write, and movement operations indefinitely.



**Data Storage (Tape)**:

- GoL can represent an infinite tape using its grid, where cells encode symbols via stable or periodic structures. The grid’s theoretical infinitude ensures unbounded memory, satisfying the Turing machine’s requirement for an infinite tape.

**Control Logic (State Machine)**:

- GoL can implement a finite state machine through glider interactions. Gliders act as signals, and their collisions with other patterns (e.g., tape cells or state structures) encode logical operations. By designing the pattern to produce specific glider outputs based on inputs, any set of transition rules can be implemented.

**Operations (Read, Write, Move)**:

- GoL’s cellular automaton rules (B3/S23—born on 3 neighbors, survive on 2 or 3) allow for dynamic behavior like glider movement and collisions, which can emulate reading (detecting a symbol), writing (modifying a cell), and movement (shifting the head). These operations are realized in the turingmachine.rle pattern through carefully constructed interactions.

ref : http://rendell-attic.org/gol/tm.htm

![image-20250501170930615](C:\Users\brand\AppData\Roaming\Typora\typora-user-images\image-20250501170930615.png)

Here the Tape is the two stack 

signal isconnect to FSM 