# Day9: Disk Fragmenter
Given a disk map which looks like:
`2333133121414131402`
Where the number represents the layout of files and free space on the disk.

So, a disk map like 12345 would represent a one-block file, two blocks of free space, a three-block file,
four blocks of free space, and then a five-block file. A disk map like 90909 would represent three nine-block
files in a row (with no free space between them).

Each file on disk also has an ID number based on the order of the files as they appear before they are rearranged,
starting with ID 0. So, the disk map 12345 has three files: a one-block file with ID 0, a three-block file with ID 1,
and a five-block file with ID 2. Using one character for each block where digits are the file ID and . is free space,
the disk map 12345 represents these individual blocks:

`0..111....22222`

We would like to move file blocks one at a time from the end of the disk to the leftmost free space block (until there
are no gaps remaining between file blocks). For the disk map 12345, the process looks like this:

```
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222.....
```

Once the disk has been defragmented we should calculate the *checksum* of the disk by adding up the result of multyplying
each of these blocks positionswith the file ID number it contains.

So for the answer above it would be `0*0 + 1*2 + 2*2 + 3*1 + 4*1 + 5*2 + 6*2 + 7*2 = 2 + 4 + 4 + 3 + 4 + 10 + 12 + 14 = 53`
