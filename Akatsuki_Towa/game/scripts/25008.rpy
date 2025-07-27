label avg25008:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210011)]'
hide p1
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210012)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210013)]'
return