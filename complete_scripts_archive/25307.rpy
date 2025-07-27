label avg25307:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7079.ogg"
c23 '[convertstrid(1211183)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1211184)]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25308
    "[textdict[1214996]]":
        call avg25309
return