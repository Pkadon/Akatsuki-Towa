label avg10111:

play music "ed7516.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1006226)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006227)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
c33 '[convertstrid(1006228)]'
hide p1
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1006229)]'
hide p3
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1006230)]'
hide p56
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
c571 '[convertstrid(1006231)]'
hide p1
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('sc051_01 1', 'p58', [r(-32), light], 6)
c583 '[convertstrid(1006232)]'
hide p58
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1006233)]'
return