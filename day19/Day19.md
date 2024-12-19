# Day 19: Linen Layout

Given a number of colred towels with colors like white (w), blue (u), black (b), red (r), or green (g),
and a number of patterns like `brwrr`

Given an input like:

```
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgw
```
What can be done with this input:

```
* brwrr can be made with a br towel, then a wr towel, and then finally an r towel.
* bggr can be made with a b towel, two g towels, and then an r towel.
* gbbr can be made with a gb towel and then a br towel.
* rrbgbr can be made with r, rb, g, and br.
* ubwu is impossible.
* bwurrg can be made with bwu, r, r, and g.
* brgr can be made with br, g, and r.
* bbrgwb is impossible.
```

## Part 1
Where the top line are the kind of towewls you have and the rest of the lines are the patterns how many
of the patterns can you make with the towels you have?

## Part 2
Of all the patterns that can be made how many different ways can they be made?
Add up and return the result for all of them.
