label avg24515:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 13', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1206039)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1206040)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1206041)]'
return