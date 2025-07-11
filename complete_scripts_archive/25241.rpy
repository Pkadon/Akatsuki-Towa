label avg25241:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_atk_01.ogg"
c13 '[textdict[1210869]]'
hide p1
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_hurt_01.ogg"
c23 '[textdict[1210870]]'
hide p2
c20143 '[textdict[1210871]]'
$ update_portrait('oc002_01 15', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch16.ogg"
c23 '[textdict[1210872]]'
hide p2
play sfx2 "other_7075.ogg"
c20143 '[textdict[1210873]]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210874]]'
hide p1
c20143 '[textdict[1210875]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210876]]'
hide p2
c20143 '[textdict[1210877]]'
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1210878]]'
return