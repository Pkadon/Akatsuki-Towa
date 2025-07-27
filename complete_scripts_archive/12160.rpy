label avg12160:

play music "ed7104.ogg"
scene avg_bg_027
$ update_narrator('c9621')
window show
with fade_in
c9621 '[convertstrid(1128430)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1128431)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c9621 '[convertstrid(1128432)]'
scene avg_bg_028
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfx2 "other_7021.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1128433)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 14', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1128434)]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1128436)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128437)]'
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c21 '[convertstrid(1128438)]'
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1128439)]'
return