label avg25016:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210033)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210034)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210035)]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25025
    "[textdict[1215000]]":
        call avg25026
return