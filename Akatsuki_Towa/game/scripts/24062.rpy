label avg24062:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1200252)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1200253)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1200254)]'
return