label avg12188:

play music "ed7103.ogg"
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1120710)]'
c0 '[convertstrid(1120711)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "other_7020.ogg"
c13 '[convertstrid(1120712)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1120713)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1120714)]'
hide p3
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1120715)]'
hide p4
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1120716)]'
hide p2
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1120717)]'
return