label avg25077:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1210233]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210234]]'
menu:
    extend ""
    "[textdict[1210240]]":
        call avg25078
    "[textdict[1210241]]":
        call avg25079
return