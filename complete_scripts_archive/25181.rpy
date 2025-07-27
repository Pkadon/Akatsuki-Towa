label avg25181:

stop music
scene placeholderbackground
$ update_narrator('c20203')
window show
with fade_in
play sfx2 "other_7077.ogg"
c20203 '[convertstrid(1210586)]'
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210587)]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1210588)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na18.ogg"
c13 '[convertstrid(1210589)]'
hide p1
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210590)]'
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfx2 "common_sephi2.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[convertstrid(1210591)]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210592)]'
return