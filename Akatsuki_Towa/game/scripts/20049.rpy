label avg20049:

play music "ED6505.ogg"
scene avg_bg_027
$ update_narrator('c5963')
window show
with fade_in
c5963 '[textdict[1002767]]'
c5963 '[textdict[1002768]]'
c5963 '[textdict[1002769]]'
c5963 '[textdict[1002770]]'
c5973 '[textdict[1002771]]'
c5973 '[textdict[1002772]]'
c5983 '[textdict[1002773]]'
c5963 '[textdict[1002774]]'
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1002775]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1002776]]'
return