# STRUCTURE and RECORD





# UNION and MAP

```fortran
structure /myunion/
union
  map
    character(2) w0, w1, w2
  end map
  map
    character(6) long
  end map
end union
end structure

record /myunion/ rec
! After this assignment...
rec.long = 'hello!'

! The following is true:
! rec.w0 === 'he'
! rec.w1 === 'll'
! rec.w2 === 'o!'
```

The two maps share memory, and the size of the union is ultimately six bytes:

```bash
0    1    2    3    4   5   6     Byte offset
-------------------------------
|    |    |    |    |    |    |
-------------------------------

^    W0   ^    W1   ^    W2   ^
 \-------/ \-------/ \-------/

^             LONG            ^
 \---------------------------/
```
UNION和MAP联合使用，可以使Structure对象的部分成员共享同一块内存。

所以当新建一个structure时，可以选择使用共享内存的成员。如同上面的

```fortran
    rec.long = 'hello!'
```
当共享内存的成员数据结构不一样时，就不能同时使用两类成员

```fortran
program test
     implicit none
     STRUCTURE /item/

         integer*4 :: a
         real*8    :: r

         UNION
         map
         integer*8 :: c
         end map

         map
         real*8    :: d
         end map
         end union

     end STRUCTURE

     RECORD /item/ u

     u%d=100.0;
     u%c=20

     write(*,*) u%d, u%c

end program
```

此时，程序的输出
```
 9.8813129168249309E-323                   20
```

也就是说，在同一个union中，使用哪一组map都是允许的。但是使用者必须明白，使用其
中一组map，会相应改变同union的其他map组的数值。

另一方面，一个编写正确的程序，不会同时使用一个union的不同map组。

ifort可以编译type定义的派生数据类型内的union和map，但是gfortran不允许这么做。
gfortran允许在f90内部使用STRUCTURE 和record，以及其内部定义的union和map，但不允
许type和union的混合使用。由上面的讨论可以知道，如果程序里面同时使用两者，在
ifort下可以编译通过，想在gfortran下编译通过，解决的办法就是删掉map和union，如果
不同组的map中有相同名称的成员，保留一个即可。代价是增加一部分的内存使用量。

经典g77的很多旧语法，我感觉都是为了减少内存使用或者处理速度，毕竟当时的内存和
CPU都是如此宝贵。

参考资料:

1. [简书文章](https://www.jianshu.com/p/5c4930c49c37)
2. [FORTRAN 77 Language Reference](https://docs.oracle.com/cd/E19957-01/805-4939/6j4m0vnbl/index.html)
3. [UNION-and-MAP](https://gnu.huihoo.org/gcc/gcc-7.1.0/gfortran/UNION-and-MAP.html)
4. [STRUCTURE and RECORD](https://gcc.gnu.org/onlinedocs/gfortran/STRUCTURE-and-RECORD.html#STRUCTURE-and-RECORD)