label avg25802:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210422)]]'
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210423)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210424)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "common_tag_2.ogg"
c00 '[textdict[str(1211254)]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211255)]]'
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211256)]]'
play sfxvoice "avg_vocal_ch31.ogg"
hide c1portrait
show oc002_01 7 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211257)]]'
play sfxvoice "avg_vocal_na05.ogg"
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211258)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211259)]]'
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211260)]]'
play sfx2 "fight_6026.ogg"
hide c1portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211261)]]'
play sfx2 "other_7034.ogg"
play sfxvoice "bcv_oc001_win_02.ogg"
hide c1portrait
show oc001_01 5 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211262)]]'
return