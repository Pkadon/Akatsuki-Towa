label avg25241:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_atk_01.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210869]]'
play sfxvoice "bcv_oc002_hurt_01.ogg"
hide c1portrait
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210870]]'
hide c2portrait
c20140 '[textdict[1210871]]'
play sfxvoice "avg_vocal_ch16.ogg"
show oc002_01 15 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210872]]'
play sfx2 "other_7075.ogg"
hide c2portrait
c20140 '[textdict[1210873]]'
play sfxvoice "avg_vocal_na02.ogg"
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210874]]'
hide c1portrait
c20140 '[textdict[1210875]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210876]]'
hide c2portrait
c20140 '[textdict[1210877]]'
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na20.ogg"
show oc001_01 10 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210878]]'
return