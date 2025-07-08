label avg24097:
stop music

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
c11 '[textdict[1200341]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c50123 '[textdict[1200342]]'
hide p1
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1200343]]'
return