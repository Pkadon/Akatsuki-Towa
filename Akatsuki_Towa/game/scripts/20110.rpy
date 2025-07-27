label avg20110:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1005374)]'
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1005375)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1005376)]'
hide p1
$ update_portrait('sc025_01 2', 'p622', [mid(-1), light], 5)
c6223 '[convertstrid(1005377)]'
hide p622
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1005378)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1005379)]'
return