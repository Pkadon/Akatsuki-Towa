label avg24073:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1200284)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1200285)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1200286)]'
return