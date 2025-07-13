label avg25021:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1210048]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210049]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210050]]'
return