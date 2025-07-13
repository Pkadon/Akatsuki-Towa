label avg25227:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "fight_6025.ogg"
c0 '[textdict[1210807]]'
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210808]]'
hide p1
play sfx2 "other_7082.ogg"
c20173 '[textdict[1210809]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210810]]'
return