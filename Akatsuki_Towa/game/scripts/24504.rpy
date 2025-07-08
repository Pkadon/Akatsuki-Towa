label avg24504:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1206005]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 5)
c23 '[textdict[1206006]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1206007]]'
return