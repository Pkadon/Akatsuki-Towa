label avg24505:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1206008)]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1206045)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1206009)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1206010)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1206011)]'
return