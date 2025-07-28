label avg25199:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210668)]'
hide p2
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1210669)]'
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1210670)]'
hide p1
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
play sfx2 "other_7085.ogg"
c20183 '[convertstrid(1210671)]'
hide p2018
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[convertstrid(1210672)]'
hide p2
$ update_portrait('uc003_01 3', 'p2018', [mid(-26), light], 6)
c20183 '[convertstrid(1210673)]'
hide p2018
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1210674)]'
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210675)]'
return