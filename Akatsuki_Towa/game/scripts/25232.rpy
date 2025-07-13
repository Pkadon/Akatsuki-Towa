label avg25232:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6024.ogg"
c23 '[textdict[1210826]]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210827]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210828]]'
return