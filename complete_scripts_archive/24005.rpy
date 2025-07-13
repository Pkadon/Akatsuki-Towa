label avg24005:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1200016]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1200017]]'
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
c13 '[textdict[1200018]]'
return