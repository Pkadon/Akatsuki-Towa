label avg25241:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_atk_01.ogg"
show oc001_01 19 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210869]]'
play sfxvoice "bcv_oc002_hurt_01.ogg"
hide p1
show oc002_01 3 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210870]]'
hide p2
c20143 '[textdict[1210871]]'
play sfxvoice "avg_vocal_ch16.ogg"
show oc002_01 15 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210872]]'
play sfx2 "other_7075.ogg"
hide p2
c20143 '[textdict[1210873]]'
play sfxvoice "avg_vocal_na02.ogg"
show oc001_01 7 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210874]]'
hide p1
c20143 '[textdict[1210875]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210876]]'
hide p2
c20143 '[textdict[1210877]]'
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na20.ogg"
show oc001_01 10 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210878]]'
return