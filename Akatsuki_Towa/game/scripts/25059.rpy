label avg25059:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1210171)]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210172)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210173)]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25080
    "[textdict[1215000]]":
        call avg25026
return