weather(phenoix,hot,summer).
weather(la,warm,summer).

warmer_than(c1,c2):-
weather(c1,hot,summer),
weather(c2,warm,summer).