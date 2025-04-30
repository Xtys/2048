Demo II -- Game Of Life

Section I

a)

Underpopulation: A live cell that has < 2 live neighbouring cells will die

Survival: A live cell that has 2-3 live neighbouring cells will remain alive

Overpopulation: A live cell with more than 3 live neighbours will die

Reproduction: A dead cell with exactly 3 live neighbours will become alive

[python - Sum of 8 neighbors in 2d array - Stack Overflow](https://stackoverflow.com/questions/36964875/sum-of-8-neighbors-in-2d-array) 



b) 

just check it , is gliding  

By running test_gameoflife_glider.py



c) 

fix line : self.grid[index[0]+6, index[1]+18] = self.aliveValue

[Gosper glider gun - LifeWiki](https://conwaylife.com/wiki/Gosper_glider_gun)

now to setup the glider gun rle?

https://stackoverflow.com/questions/45577236/game-of-life-rle-format-line-ending-with-number



d) [#413](https://edstem.org/au/courses/22228/discussion/2609614)

get 3 patterns from https://conwaylife.com/wiki/LifeWiki:News_archive

![image-20250429225056163](C:\Users\brand\AppData\Roaming\Typora\typora-user-images\image-20250429225056163.png)

![image-20250429225216345](C:\Users\brand\AppData\Roaming\Typora\typora-user-images\image-20250429225216345.png)

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



g)

h)

i) ![image-20250429231327783](C:\Users\brand\AppData\Roaming\Typora\typora-user-images\image-20250429231327783.png)