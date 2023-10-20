female(pam).
female(liz).
female(pat).
female(ann).

male(jim).
male(bob).
male(tom).
male(peter).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(bob,peter).
parent(peter,jim).

mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),female(X).
sister(X,Y):-parent(Z,Y),parent(Z,X),female(X),X\==Y.
brother(X,Y):-(X,Y):-parent(Z,Y),parent(Z,X),male(X),X\==Y.
