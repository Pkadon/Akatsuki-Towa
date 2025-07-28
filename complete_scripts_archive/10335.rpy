label avg10335:

play music "ed9998.ogg"
scene avg_bg_061
$ update_narrator('c41')
window show
with fade_in
$ update_portrait('oc004_01 2', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[convertstrid(1130999)]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1131024)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131011)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[convertstrid(1131012)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131013)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro05.ogg"
c31 '[convertstrid(1131014)]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 12', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1131015)]'
hide p5
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1131016)]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
c41 '[convertstrid(1131017)]'
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131018)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131019)]'
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 10', 'p5', [l_entrance(-6), light, flip], 6)
c51 '[convertstrid(1131020)]'
$ update_portrait('oc005_01 10', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1131021)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1131022)]'
hide p5
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch13.ogg"
c21 '[convertstrid(1131023)]'
return