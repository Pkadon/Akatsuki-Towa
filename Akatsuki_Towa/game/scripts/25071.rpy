label avg25071:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1210223]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210224]]'
menu:
    extend ""
    "[textdict[1210240]]":
        call avg25072
    "[textdict[1210241]]":
        call avg25072
return