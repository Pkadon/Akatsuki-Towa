label avg12408:

play music "ed7100.ogg"
scene avg_bg_049
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 5', 'p1', [r_entrance(-2), light], 6)
play sfx2 "common_wheel.ogg"
c13 '[convertstrid(1142528)]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1142529)]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c31 '[convertstrid(1142530)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1142531)]'
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1142532)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r_entrance(-5), light], 6)
c43 '[convertstrid(1142533)]'
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1142534)]'
hide p2
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1142535)]'
hide p4
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1142536)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1142537)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[convertstrid(1142538)]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1142539)]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1142540)]'
hide p4
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1142541)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r_entrance(-5), light], 6)
c43 '[convertstrid(1142542)]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1142543)]'
hide p4
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1142544)]'
return