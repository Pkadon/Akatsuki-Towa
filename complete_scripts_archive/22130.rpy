label avg22130:
stop music

scene avg_bg_036
with fade
play sfxvoice "avg_vocal_ro15.ogg"
show oc003_01 9 as c3portrait at centerpos(-6), zorder 5
c33 '[textdict[1128262]]'
hide c3portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1128263]]'
hide c2portrait
show oc001_01 3 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1128264]]'
hide c1portrait
show oc003_01 10 as c3portrait at centerpos(-6), zorder 5
c33 '[textdict[1128265]]'
play sfx2 "fight_6024.ogg"
hide c3portrait
show oc001_01 20 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1128266]]'
return