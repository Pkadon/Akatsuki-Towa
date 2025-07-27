label avg22192:

play music "ed7110.ogg"
scene avg_bg_013
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1120751)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1120752)]'
return