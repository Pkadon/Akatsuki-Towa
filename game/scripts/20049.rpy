label avg20049:
stop music

play music "ED6505.ogg"
scene avg_bg_027
with fade
c5960 '[textdict[str(1002767)]]'
c5960 '[textdict[str(1002768)]]'
c5960 '[textdict[str(1002769)]]'
c5960 '[textdict[str(1002770)]]'
c5970 '[textdict[str(1002771)]]'
c5970 '[textdict[str(1002772)]]'
c5980 '[textdict[str(1002773)]]'
c5960 '[textdict[str(1002774)]]'
play sfxvoice "avg_vocal_ch08.ogg"
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1002775)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1002776)]]'
return