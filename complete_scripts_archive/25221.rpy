label avg25221:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6025.ogg"
c13 '[convertstrid(1210766)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210767)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210768)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfx2 "elc_5003.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210769)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1210770)]'
return