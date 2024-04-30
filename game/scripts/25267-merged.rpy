label avg25267:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7050.ogg"
c20130 '[textdict[str(1211005)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25268
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na06.ogg"
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211008)]]'
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211009)]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211010)]]'
play sfxvoice "avg_vocal_ch07.ogg"
hide c1portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211011)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na13.ogg"
show oc001_01 9 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211012)]]'
play sfx2 "other_7079.ogg"
hide c1portrait
c20130 '[textdict[str(1211013)]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211014)]]'
play sfxvoice "avg_vocal_na10.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211015)]]'
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211016)]]'
play sfx2 "fight_6003.ogg"
hide c2portrait
c20130 '[textdict[str(1211017)]]'
show oc002_01 11 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211018)]]'
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na15.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211019)]]'
return