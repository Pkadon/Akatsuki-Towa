label avg24510:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1206023]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1206024]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1206025]]'
return