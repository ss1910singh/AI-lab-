parent(joe, jane).
parent(harry, carl).
parent(meg, jane).
parent(jane, anne).
parent(carl, ralph).
parent(hazel, harry).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
