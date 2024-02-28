4-squares cipher
================

From the given plaintext fragment "filesareopened", we can recover the following mappings:

    fi --» CB
    le --» JP
    sa --» KE
    re --» SP
    op --» EU
    en --» HL
    ed --» HA

This gives the following partial squares:

    a b c d e   - - - H -
    f g h i j   - - - C -
    k l m n o   E - - - J
    p r s t u   K - - - S
    v w x y z   - - - - -

    - P E - A   a b c d e
    B - - - -   f g h i j
    - - - - L   k l m n o
    - - - - U   p r s t u
    - - - - -   v w x y z

We can continue with the other plaintext fragments given in the same way. We must be careful in identifying the right 2-gram boundaries, though. For instance, the plaintext word 'encoded' does not start at a 2-gram boundary, so we can only use the letter pairs nc, od, and ed from it (moreover, ed has already be mapped). This gives the following mappings and partial squares:

    nc --» GN
    od --» IA
    ea --» PA
    da --» PN
    nd --» IN
    wr --» VR
    it --» CT
    te --» SN
    on --» IL
    ta --» KN
    in --» CK

    a b c d e   P - - H -
    f g h i j   - - - C -
    k l m n o   E - G I J
    p r s t u   K - - - S
    v w x y z   - V - - -

    - P E N A   a b c d e
    B - - - -   f g h i j
    - - - K L   k l m n o
    - R - T U   p r s t u
    - - - - -   v w x y z

We can then continue with guessing the bottom left square and the upper right square...

    a b c d e   P Y T H O
    f g h i j   N A B C D
    k l m n o   E F G I J
    p r s t u   K L M R S    
    v w x y z   U V W X Z

    O P E N A   a b c d e
    B C D F G   f g h i j
    H I J K L   k l m n o
    M R S T U   p r s t u
    V W X Y Z   v w x y z
