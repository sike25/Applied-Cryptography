4-squares cipher
================

We intercepted the following ciphertext produced with the 4-squares cipher:

    JKMIYHIWCBJPKESPEUHLHACKSNXSJJON
    MFHMJEHHRXJUSPHOHHYYRCSNRSRCFFKD
    SIEEINSKMFPGAKYZCDTDYMOAGNIAHACK
    TMSOHDCBOEGNIACKCCDOGNIACKCCRJIU
    KSTANFDNHTDEONNOLLRFKSEPKFFUIEPU
    HLONITSEOLSOFNPMSOINHASKMFTLIAOL
    SOGTMFPGAKHGFNCKYMWKIAHLFZMFHAHM
    HBLSPAPNINVRCTSNIFITDEDHMIEGHWSN
    SJOCTAMTMFBTJJONMDJUIPOPMUHADHKP
    FICBJPRSNERNILMNILKNCKSNXS

We know a few words from the corresponding plaintext:

    ........filesareopened..........
    ................................
    .......................encoded..
    ................................
    ................................
    ................................
    ................................
    ...readandwritten...............
    ................................
    ...............contain.... 

Can you recover the squares that define the coding and decrypt the ciphertext?

## Hints

The plaintext squares contain the standard alphabet (letters are in the right order) and letter q is omitted (to reduce the alphabet size to 25): 

    a b c d e   - - - - -
    f g h i j   - - - - -
    k l m n o   - - - - -
    p r s t u   - - - - -
    v w x y z   - - - - -

    - - - - -   a b c d e
    - - - - -   f g h i j
    - - - - -   k l m n o
    - - - - -   p r s t u
    - - - - -   v w x y z

The task is to recover the upper-right and bottom-left squares. Each of those is constructed by starting with a keyword and then continuing with the remaining letters of the alphabet in order. For instance, if the keyword was KEYWORD, then the square would look like this:

    K E Y W O
    R D A B C
    F G H I J
    L M N P S
    T U V X Z

You can find a description of the operation of the 4-square cipher at [http://en.wikipedia.org/wiki/Four-square_cipher](http://en.wikipedia.org/wiki/Four-square_cipher).

