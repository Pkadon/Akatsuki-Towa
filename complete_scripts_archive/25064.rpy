label avg25064:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1210190)]'
hide p2
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210191)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210192)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210193)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210194)]'
menu:
    extend ""
    "[textdict[1210238]]":
        call avg25065
    "[textdict[1210239]]":
        call avg25066
return