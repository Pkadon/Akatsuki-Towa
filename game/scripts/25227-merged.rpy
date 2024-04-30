label avg25227:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6025.ogg"
c00 '[textdict[str(1210807)]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210808)]]'
play sfx2 "other_7082.ogg"
hide c1portrait
c20170 '[textdict[str(1210809)]]'
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210810)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6003.ogg"
play sfxvoice "bcv_oc002_win_02.ogg"
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210811)]]'
hide c2portrait
show oc001_01 20 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210812)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na03.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210813)]]'
play sfx2 "other_7082.ogg"
hide c1portrait
c20170 '[textdict[str(1210814)]]'
play sfx2 "elc_5004.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210815)]]'
hide c2portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210816)]]'
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210817)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7059.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210818)]]'
play sfx2 "common_36rewardsp.ogg"
hide c2portrait
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210819)]]'
return