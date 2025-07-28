label avg10374:

play music "ed7151.ogg"
scene avg_bg_023
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
window show
with fade_in
c43 '[convertstrid(1132127)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1132128)]'
$ update_portrait('oc004_01 14', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1132129)]'
hide p4
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1132130)]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1132131)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1132132)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 1', 'p1043', [l(-19), light, flip], 6)
c10431 '[convertstrid(1132133)]'
hide p2
$ update_portrait('st040_01 1', 'p1043', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1132134)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1132135)]'
hide p1
$ update_portrait('oc003_01 6', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1132136)]'
hide p1043
$ update_portrait('oc003_01 6', 'p3', [r(-6), dark], 5)
$ update_portrait('sc048_01 3', 'p55', [l(-7), light, flip], 6)
c551 '[convertstrid(1132137)]'
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
c551 '[convertstrid(1132138)]'
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
c551 '[convertstrid(1132139)]'
hide p3
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1132140)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1132141)]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
c551 '[convertstrid(1132142)]'
$ update_portrait('sc048_01 3', 'p55', [l(-7), light, flip], 6)
c551 '[convertstrid(1132143)]'
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
c551 '[convertstrid(1132144)]'
hide p2
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1132145)]'
hide p55
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1132146)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1132147)]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1132148)]'
menu:
    extend ""
    "[textdict[1132149]]":
        call avg10375
    "[textdict[1132150]]":
        call avg10376
    "[textdict[1132151]]":
        call avg10377
return