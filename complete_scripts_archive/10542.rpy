label avg10542:

play music "ed7151.ogg"
scene avg_bg_078
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1152695)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1152696)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1152697)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152698)]'
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152699)]'
hide p3
hide p1
$ update_portrait('st040_01 5', 'p239', [l(-19), light, flip], 6)
$ update_narrator('c2391')
with fade
c2391 '[convertstrid(1152700)]'
$ update_portrait('st040_01 5', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
c43 '[convertstrid(1152701)]'
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1152702)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152703)]'
return